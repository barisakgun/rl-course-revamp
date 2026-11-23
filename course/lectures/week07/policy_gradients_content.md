# Policy gradients · first-render content

**Historical: frozen at the first render (2026-11-23).** The PPTX is the source from that render on; status is in the [deck decisions](../../../decisions/lectures/policy_gradients.md).

Shared · ChatGPT · 2026-11-23. One deck for sessions 7.1 and 7.2. Use the headings as slide titles, omitting IDs and minutes from the screen. Put the ID, timing, sources, answer cues and qualifications in speaker notes. Reveal worked answers after the prompt. Freeze this file at the first render. [Deck decisions and status](../../../decisions/lectures/policy_gradients.md) · [Shared review](../../../analysis/lecture_suggestions/policy_gradients_review.md) · [Notation](../../notation_guide.md)

## Renderer handoff

P numbers are **editable PPTX slide positions**, including hidden slides, in [7 – Policy Space Methods](<../../../sources/current_course/7 - Policy Space Methods.pptx>). DPG numbers refer to [9 – Deep PG](<../../../sources/current_course/9 - Deep PG.pptx>). Copy the named shapes, images and equation objects. Replace inherited labels, notes and formulas where specified. All fork diagrams and tables are new. Use the same left/right labels, branch positions and colors throughout. Title frame: “Policy gradients” / COMP 438/538 Introduction to Reinforcement Learning / Barış Akgün / Fall 2026. Present the title while opening P01. Show the session boundary at B01. There is one live route.

| Session | Timed blocks | Delivery target |
| --- | --- | ---: |
| 7.1 | Pendulum 2 + motivations 2 + history 10 + parameterization 9 + derivation and sample setup 40 (includes the 2-minute Gaussian score) | 63 teaching |
| 7.2 | Finish sample 8 + Puck World 4 + baselines and evaluation 22 + advantages and learned baseline 12 + critic motivation and bias 12 | 58 teaching + 5 administration |

Each session leaves seven minutes of the scheduled 70. Protect the ten minutes for history and the opening eight-minute student calculation in 7.2. Old P49–52 provide material for 8.1; use only P51’s conditional-mean identity in B09. No appendix for P54–58 or P60–63. Use only the source attributions specified in the live material. After the first render, remind the instructor of the D4 historical checks (Kohl and Stone, Szita and Lőrincz, Salimans et al., Williams including the acronym, and Sutton et al.). Carry the verify flags in preparation notes. Baxter et al. was checked separately.

## 7.1 · Policy search and REINFORCE

### P01 · Which torque keeps the pendulum upright? · 2 min

Use the pendulum drawing from P41. Replace the old angle and control symbols with the words **angle** and **torque**. Display “We can run the pendulum and observe its motion. Which information should the controller use?” Reveal this classroom MDP: state = angle and angular velocity; action = signed torque; reward = +1 for each transition ending within the upright range; episode ends on leaving that range.

**Notes.** Start near upright. At the same angle the pendulum can move toward upright or fall away. Velocity distinguishes those situations. The physical dynamics are unknown to the learner. Week 6’s DQN compared one output per discrete action. With continuously variable torque, finding the greedy torque would itself require an optimization. Introduce the alternative of directly producing an action distribution.

### P02 · Why represent the policy directly? · 2 min

Reuse P4–6’s comparison picture, keeping only the state → policy → action path. Display four reasons: produce a continuous action directly; learn how often to choose each action; express a simple control rule or prior knowledge about its form; change probabilities smoothly as preferences change.

**Notes.** A corridor with an exit to the right can have a one-line rule even though values vary with distance. A small change in either of two nearly tied Q estimates can flip the greedy action. In games such as rock–paper–scissors, mixing actions can itself be the strategy. S01 gives the single-agent example. Avoid a blanket convergence claim.

### H01 · A controller can be scored by a trial · 3 min

Reuse the starting and trained AIBO gait photos from P27 and the gait-parameter illustration from P28. Display “Choose gait parameters → walk the course → measure traversal time.” Ask “What observation would let us rank two parameter settings?” Reveal “Higher return = shorter traversal time.” Introduce \(J(\boldsymbol\theta)\) as the expected trial return.

**Notes.** Take negative time as the return for a completed trial under a common protocol. A parameter vector specifies the controller throughout that trial. A noisy trial supplies one estimate. Old P27 attributes the gait study to Kohl and Stone (2004); retain **verify** for the original attribution/details under D4. Avoid numerical performance claims.

### H02 · Cross-entropy search over controllers · 4 min

Reuse P18–19’s population pictures, labeling a dot “one controller.” Place these steps beside them: sample parameter vectors from a Gaussian; evaluate the sampled controllers; keep the top-scoring fraction; fit the next mean and spread to that fraction. Repeat. Ask students to identify what moved between the two pictures.

**Notes.** It is the distribution over candidate controller parameters. Later the Gaussian on S03 is a distribution over torques for one controller in one state. P17–20 supply the historical example. Retain **verify** if discussing Szita and Lőrincz’s Tetris result or later evolution strategies (Salimans et al.); neither claim is needed live.

### H03 · Which parameter change improves the gait? · 3 min

Keep the forward-difference equation from P24, with course notation:
\[
\frac{\partial J(\boldsymbol\theta)}{\partial \theta_k}\ \approx\
\frac{J(\boldsymbol\theta+\epsilon\mathbf u_k)-J(\boldsymbol\theta)}{\epsilon}.
\]
Label the two trials “one setting perturbed” and “reference setting.” Ask “Which data did we use from each run? What else did we collect?”

**Notes.** \(\mathbf u_k\) changes coordinate \(k\) only; ε is a small perturbation. For all coordinates, one reference setting plus one perturbed setting per coordinate suffices, with repeated runs as needed at each setting. Matched random conditions can reduce comparison noise. Here we compared whole-run returns. Actions, states and the timing of rewards will now let us assign credit within a run. Recognition only.

### S01 · When always going right gets you stuck · 3 min

Use the corridor drawing and performance curve from Sutton & Barto, Example 13.1, printed p. 323 / PDF p. 345. First show the drawing: start at the left end; there are three decision states; right/left have reversed effects in the middle state; each step costs 1. “All three states have the same policy features. Trace always-right. Now trace always-left.” Reveal the curve: the best shared probability of right is about 0.59.

**Notes.** Always-right cycles between the first two cells. Always-left stays at the start. A stochastic memoryless policy can produce the required right–left–right sequence. The graph shows expected start return (about −11.6 at the peak) and motivates learning the probability. Do not ask for a corridor calculation. [Book example](../../../sources/RLbook2020.pdf#page=345)

### S02 · Turn action preferences into probabilities · 3 min

Adapt P13–14’s discrete policy and DPG 8’s output sketch. Show a state producing one preference per action and a softmax producing probabilities:
\[
\pi(a\mid s,\boldsymbol\theta)=
\frac{\exp h(s,a,\boldsymbol\theta)}{\sum_{b\in\mathcal A(s)}\exp h(s,b,\boldsymbol\theta)} .
\]
For the upcoming fork set the right preference to scalar θ and the left preference to zero in every state. Display \(\pi(\mathrm{right}\mid s,\theta)=e^\theta/(1+e^\theta)\). Ask what the agent does at θ = 0.

**Notes.** It samples right or left with equal probability. Increasing θ makes right more likely. A preference specifies relative likelihood; its units differ from expected return. The shared preference is sufficient to favor right at all three fork states.

### S03 · A distribution over pendulum torques · 3 min

Reuse P15’s one-dimensional Gaussian density and P41’s pendulum. Display
\[
\pi(a\mid s,\boldsymbol\theta)=
\frac{1}{\sigma(s,\boldsymbol\theta)\sqrt{2\pi}}
\exp\!\left[-\frac{(a-\mu(s,\boldsymbol\theta))^2}{2\sigma(s,\boldsymbol\theta)^2}\right].
\]
Draw two torque densities with the same mean and different spreads. Ask “Which controller tries torques farther from its mean more often?”

**Notes.** Sample one torque at each decision. The mean depends on angle and angular velocity. A wider density increases spread. The mean μ here differs from the policy-dependent state distribution \(\mu^\pi(s)\) used in Week 5. Use an idealized real-valued commanded torque. D03 uses a fixed spread and linear mean.

### D01 · What changes when the policy changes? · 3 min

Adapt P16 and P21–22. Show \(J(\boldsymbol\theta)=v^{\pi_{\boldsymbol\theta}}(s_0)=\mathbb E_{\pi_{\boldsymbol\theta}}[G_0]\), with \(G_0=\sum_{t=0}^{T-1}\gamma^t R_{t+1}\). Display the fork:

| State | Right | Left |
| --- | --- | --- |
| Start | Reward 2 → upper | Reward 2 → lower |
| Upper | Reward 4 → terminal | Reward 2 → terminal |
| Lower | Reward 2 → terminal | Reward 0 → terminal |

Draw as a two-level tree, γ = ½. Ask “If the policy chooses right more often, which observations in our training data change?”

**Notes.** Both action frequencies and visits to upper/lower change. The numbers printed on the branches stay fixed. We need the derivative of expected return with respect to the policy parameters. First examine the last decision in isolation.

### D02a · One decision gives a gradient we can check · 4 min

Adapt P33–34. Isolate the upper branch as a one-step problem: right earns 4, left earns 2. Render
\[
J(\theta)=\sum_a \pi(a\mid \mathrm{upper},\theta)\mathcal R(a),\qquad
\nabla\pi(a\mid s,\theta)=\pi(a\mid s,\theta)\nabla\log\pi(a\mid s,\theta).
\]
Reveal \(\nabla J(\theta)=\mathbb E_\pi[\mathcal R(A_0)\nabla\log\pi(A_0\mid \mathrm{upper},\theta)]\) for this one-step objective. Label the log-probability gradient **score**.

**Notes.** The first \(J\) on this slide starts at upper. Expand the two-action sum, differentiate the probabilities and use the log derivative to turn the result into an expectation under the sampling policy. Positive movement along a nonzero score increases the sampled action’s log probability locally. The book also calls this the “eligibility vector.” Return to the original start-state objective on D04.

### D02b · Check the score before trusting a sample · 3 min

Keep the binary policy from S02 visible. Differentiate \(\log\pi(\mathrm{right})=\theta-\log(1+e^\theta)\) and \(\log\pi(\mathrm{left})=-\log(1+e^\theta)\). Reveal the two scores \(1-\pi(\mathrm{right})\) and \(-\pi(\mathrm{right})\). At θ = 0, ask pairs to fill the last column.

| Upper action | Probability | Score | Reward × score |
| --- | ---: | ---: | ---: |
| Right | ½ | +½ | **2** |
| Left | ½ | −½ | **−1** |

**Notes.** Average of the last column = ½. Direct check: expected reward is \(2+2\pi(\mathrm{right})\), whose derivative at zero is \(2(½)(½)=½\). A left sample favors left even though right is better; the right contribution is larger on average. Use this same table again in B05.

### D03 · What does the torque score change? · 2 min

Adapt P37, keeping only the mean-parameter score. Put \(\mu(s,\boldsymbol\theta)=\boldsymbol\theta^\top\mathbf x(s)\) and fixed spread σ beside the S03 density. Reveal
\[
\nabla\log\pi(a\mid s,\boldsymbol\theta)
=\frac{a-\mu(s,\boldsymbol\theta)}{\sigma^2}\mathbf x(s).
\]
Mark a sampled torque to the right of the mean. “A better-than-expected result gives this score positive weight. Which way does the mean move at this state?”

**Notes.** Toward the sampled torque. Differentiating the quadratic log-density with respect to its mean gives \((a-\mu)/\sigma^2\); differentiating the mean supplies the features. Hold σ fixed here. No pendulum arithmetic.

### D04a · What is the probability of this episode? · 4 min

Reuse P40’s board-derivation slot. Show one fork path and the general factorization beside it:
\[
\Pr\{\tau\mid\boldsymbol\theta\} =
\Pr\{S_0=s_0\}
\prod_{t=0}^{T-1}\pi(a_t\mid s_t,\boldsymbol\theta)
\,\mathcal M(s_t,a_t,r_{t+1},s_{t+1}).
\]
Highlight the policy factors. “Which factors change directly when we change the policy parameters?”

**Notes.** τ is a realized episode; its entries are the lower-case values in this expression. Here τ means trajectory; in Week 6 it denoted the Polyak update rate. The fixed start and environment dynamics do not depend on the parameters. Their probabilities still influence which paths we observe. A finite, differentiable policy with fixed support suffices for this board example.

### D04b · Differentiate the path likelihood · 3 min

Build from “expected return = sum over paths of probability × return.” Use \(G_0(\tau)\) as the realized discounted return, then reveal:
\[
\begin{aligned}
\nabla J(\boldsymbol\theta)
&=\sum_\tau G_0(\tau)\Pr\{\tau\mid\boldsymbol\theta\}
                   \nabla\log\Pr\{\tau\mid\boldsymbol\theta\}\\
&=\mathbb E_{\pi_{\boldsymbol\theta}}\!\left[
G_0\sum_{t=0}^{T-1}\nabla\log\pi(A_t\mid S_t,\boldsymbol\theta)\right].
\end{aligned}
\]

**Notes.** Apply the one-decision identity to a whole path. The log of D04a’s product is a sum. The parameter-independent factors drop out of the derivative. Sampling episodes handles the distribution of visited states.

### D05a · Which reward can the second action influence? · 4 min

Draw \(A_0\ \to R_1\ \to A_1\ \to R_2\) on the fork. Give students the last action’s full-return term \((R_1+\gamma R_2)\nabla\log\pi(A_1\mid S_1,\boldsymbol\theta)\). Ask which reward has already been received. At the upper branch and θ = 0 reveal the mean contribution of that reward: \(2[½(+½)+½(-½)]=0\).

**Notes.** Condition on the history immediately before \(A_1\). The earlier reward is then fixed. The current action still follows the policy, whose score averages to zero. This removes the earlier reward *in expectation*; individual score-weighted samples change.

### D05b · Assign each action its reward-to-go · 4 min

Color the prefix before decision \(t\) gray and highlight the remaining rewards:
\[
G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1},\qquad
\nabla J(\boldsymbol\theta)=\mathbb E_{\pi_{\boldsymbol\theta}}\!\left[
\sum_{t=0}^{T-1}\gamma^tG_t\,\nabla\log\pi(A_t\mid S_t,\boldsymbol\theta)\right].
\]
“Where did the outer factor come from?” Reveal the decomposition \(G_0=\sum_{k=0}^{t-1}\gamma^k R_{k+1}+\gamma^t G_t\).

**Notes.** The conditional zero-mean argument from D05a removes the prefix. The inner powers count time from the current decision. The outer discount carries the remaining rewards back to the episode start.

### D06 · Two ways time enters the update · 2 min

Display **mean over the four fork episodes at θ = 0**.

| Weight on the score | Mean contribution summed over the episode |
| --- | ---: |
| Start-state discounted objective, \(\gamma^tG_t\), γ = ½ | 0.50 |
| Give late decisions full weight, \(G_t\), γ = ½ | 0.75 |
| Undiscounted objective, γ = 1 | 1.00 |

On screen: “Keeping the discount inside the return shortens the credit horizon. Dropping the outer discount gives later decisions full weight.”

**Notes.** Most policy-gradient code drops the outer factor. This deliberate approximation can be useful when late decisions matter. It generally changes the expected direction and need not correspond to either exact objective. These three numbers are means; B01 works a single episode. At θ = 0 the discounted first-decision contribution averages ¼. The final decision contributes ¼ with the outer discount or ½ without it. With γ = 1, the first contribution also becomes ½. [Schulman et al., §2](https://arxiv.org/abs/1506.02438) · [Nota and Thomas](https://arxiv.org/abs/1906.07073)

### D07a · The policy-gradient theorem · 3 min

Adapt P35 to the start-state objective. Reveal the conditional mean and substitute it directly into D05b:
\[
\mathbb E_\pi[G_t\mid S_t=s,A_t=a]=q^\pi(s,a),\qquad
\nabla J(\boldsymbol\theta)=\mathbb E_{\pi_{\boldsymbol\theta}}\!\left[
\sum_{t=0}^{T-1}\gamma^t q^{\pi_{\boldsymbol\theta}}(S_t,A_t)
\nabla\log\pi(A_t\mid S_t,\boldsymbol\theta)\right].
\]
Footer: “Proof in Sutton & Barto §13.2, boxed argument on p. 325.”

**Notes.** The score is fixed given state/action, so replacing the sampled weight by its conditional mean preserves the expectation at each step. The time-summed form keeps the correct state weighting. The book’s box treats the undiscounted episodic case; Exercise 13.2 asks about discounting. [PDF p. 347](../../../sources/RLbook2020.pdf#page=347)

### D07b · REINFORCE from one completed episode · 4 min

Adapt P38–39. Display as a single algorithm box:

1. Collect one complete episode with policy parameters **θ** fixed.
2. Set \(G_T=0\). Work backward: \(G_t\leftarrow R_{t+1}+\gamma G_{t+1}\).
3. Evaluate all scores at the collecting policy. Form \(\hat g=\sum_{t=0}^{T-1}\gamma^tG_t\nabla\log\pi(A_t\mid S_t,\boldsymbol\theta)\).
4. Ascend once: \(\boldsymbol\theta\leftarrow\boldsymbol\theta+\alpha_{\boldsymbol\theta}\hat g\). Collect fresh experience.

**Notes.** A batch version averages episode sums before the update. Reward-to-go supplies the unknown action value in expectation. If using gradient descent, minimize the negative weighted log-probability sum, treating the weights as data. Distinguish this fixed-parameter episode update from the book’s step-loop pseudocode. Retain **verify** for the Williams (1992) historical attribution and acronym expansion in D4; omit the expansion from the slide.

### D08 · Record the episode before updating · 4 min

Return to D01’s full fork. Show “θ = 0, γ = ½, \(\alpha_{\boldsymbol\theta}=0.1\). Start → **right** → upper → **left** → terminal.” Give the class this table, with the last three columns initially blank.

| \(t\) | Action | \(R_{t+1}\) | Which rewards enter \(G_t\)? | Score sign | Weighted contribution |
| ---: | --- | ---: | --- | --- | --- |
| 0 | Right | 2 | First and second | + | |
| 1 | Left | 2 | Second | − | |

**Notes.** Students fill the reward membership and score signs. Reveal those two columns before the break. Keep the weighted contributions for B01. Reuse the same rendered tree and table there.

## 7.2 · Sampled gradients, baselines and critic motivation

### B01 · Which way does one episode move the policy? · 8 min

Open on D08’s episode and table. Ask students to compute both returns, both score-weighted terms, the update and the direction of change in the probability of right. Reveal by column.

| \(t\) | Action | \(G_t\) | Score | \(\gamma^t\) | Contribution |
| ---: | --- | ---: | ---: | ---: | ---: |
| 0 | Right | 3 | +½ | 1 | +1.5 |
| 1 | Left | 2 | −½ | ½ | −0.5 |

Reveal \(\hat g=1,\quad\theta\leftarrow 0+0.1(1)=0.1\). “What would using the full return for both actions give on this same episode?” Reveal \(3(+½-½)=0\).

**Notes.** Give students time to work before revealing the answer. Right becomes more likely (about 0.525). Full-return and reward-to-go estimators both average 0.5 here over fresh episodes. Using reward-to-go with the outer discount omitted gives 0.5 *on this episode*; γ = 1 gives 1. D06’s 0.5/0.75/1.0 were expectations. First psychology cue: Thorndike’s law of effect connects consequences with changes in the tendency to repeat an action. Here the two sampled terms pull the same parameter in opposite directions. [Book §14.3](../../../sources/RLbook2020.pdf#page=379)

### B02a · How does the puck choose its thrust? · 2 min

Reuse the puck illustration from P43 (Silver lecture 7 p. 22, original Fig. 11). Crop to the illustration, replacing the old action description. Show “Target changes. Reward at each decision = −distance to target.” Beside the image draw the published controller: **puck position, velocity and target displacement → four softmax probabilities → sample one thrust command**. Ask “How would you change the output for freely adjustable horizontal and vertical force?” Reveal “Output a mean force on each axis and sample a two-component force.”

**Notes.** This question redesigns the action interface. The published controller selected among four fixed thrust commands, and could change its command every 0.1 simulated seconds. Its six inputs are two position coordinates, two velocity components and two target-offset components. Training reset puck position, velocity and target location every 30 simulated seconds in a continuing task. The illustrated trajectory retained the puck position at resets. A full simulator state includes the phase of that reset clock. For the redesign, two Gaussian means and chosen positive spreads suffice for independent components. Connect to the pendulum, without deriving a multivariate score. [Baxter, Bartlett & Weaver, §§5.2.1–5.2.2 and Fig. 11](https://ocw.mit.edu/courses/2-997-decision-making-in-large-scale-systems-spring-2004/1d0bbfb96c884828c39f5cea5c16daf8_baxter01b.pdf#page=18)

### B02b · How much experience did improvement take? · 2 min

Use original Fig. 9 from the same paper, printed p. 370, or crop only that graph from P43. Keep both axes, units and error bars. Display the attribution and “96 of 100 training runs in this mean; four other runs appear in Fig. 10.” Ask “What does the horizontal axis count? How would we measure variability in a *gradient* estimate?”

**Notes.** Average reward is plotted against simulated puck-world iterations. The curve improves substantially and extends past \(10^8\) iterations. Training used CONJPOMDP with GPOMDP gradient estimates. The paper evaluated performance over one million simulated iterations and reported four poorer runs separately. It does not specify the Fig. 9 bar formula. This plot measures performance and the amount of experience used; high gradient variance is a possible contributor to training difficulty. To measure gradient variance, freeze a policy, collect independent samples and examine the spread of their gradients. Do this next on the fork. [Original Fig. 9](https://ocw.mit.edu/courses/2-997-decision-making-in-large-scale-systems-spring-2004/1d0bbfb96c884828c39f5cea5c16daf8_baxter01b.pdf#page=20)

### B03 · Better than what the policy usually gets? · 4 min

Reuse D02b’s upper-state table. Both rewards are positive. Ask “After a left action earns 2, should left become more likely at this state?” Reveal the usual return here, \(½(4)+½(2)=3\). Center both returns at 3. The right outcome is +1 above expectation; the left outcome is −1 below it.

**Notes.** The categorical action draw produces different sample gradients at exactly the same policy. Centering changes the sign of the weight for the worse action. Ask whether altering both sample weights has also changed their mean gradient. Let B04 establish the general result before B05 checks the spread.

### B04 · Why subtracting a state baseline works · 7 min

Reuse P44’s baseline identity. Show, for a fixed state \(s\),
\[
\begin{aligned}
\mathbb E_\pi[b(s)\nabla\log\pi(A_t\mid s,\boldsymbol\theta)\mid S_t=s]
&=b(s)\sum_a\pi(a\mid s,\boldsymbol\theta)\nabla\log\pi(a\mid s,\boldsymbol\theta)\\
&=b(s)\nabla\sum_a\pi(a\mid s,\boldsymbol\theta)=0 .
\end{aligned}
\]
Ask students to identify which step needs action independence. Reveal the episode estimator
\[
\hat g=\sum_{t=0}^{T-1}\gamma^t\big[G_t-b(S_t)\big]\nabla\log\pi(A_t\mid S_t,\boldsymbol\theta).
\]

**Notes.** Start at the state, average over its actions, then average over visited states. The outer time weight preserves the cancellation. A random baseline fixed from prior data works by conditioning on that data. Ask what happens at the upper state if we subtract the chosen action’s own deterministic reward: every update becomes zero. In this unit \(b(s)\) is the baseline; \(b(a\mid s)\) previously denoted behavior policy.

### B05 · Same expected update, different spread · 7 min

At the upper state, θ = 0. Ask students to calculate the two entries for baseline 3, then the column means and variances. Use progressive reveals. All entries are local score contributions before the common outer time weight.

| Upper action | Score | \(G_t\) × score | \((G_t-3)\) × score | \((G_t-10)\) × score |
| --- | ---: | ---: | ---: | ---: |
| Right, reward 4 | +½ | 2 | 0.5 | −3 |
| Left, reward 2 | −½ | −1 | 0.5 | 4 |
| Mean | | 0.5 | 0.5 | 0.5 |
| Variance | | 2.25 | 0 | 12.25 |

**Notes.** Reveal the baseline-10 column after asking whether a larger baseline helps. Compute the variance by weighting squared deviations from 0.5 equally. Zero spread here concerns one component at one state, with deterministic final rewards and equal action probabilities. It need not occur over complete episodes or make the exact state value the minimum-variance baseline in general.

### B06 · What would count as faster learning? · 4 min

Use Sutton & Barto **Fig. 13.2**, printed p. 330 / PDF p. 352. Preserve the axes, the two learning curves, their step-size labels and the horizontal optimal-value reference. Ask “At episode 400, what has been held equal across the curves? If our budget is environment interactions, what else should we count?”

**Notes.** The plot reports episode return averaged over 100 runs on the short corridor. It shows a learned value baseline can accelerate learning in this example. The green baseline curve uses actor step size 2⁻⁹ and value step size 2⁻⁶. The red plain REINFORCE curve uses 2⁻¹³, its best setting among the powers of two compared for plain REINFORCE. The gray horizontal line marks the optimal start value. Ask what these different step sizes allow us to conclude about the two training procedures. Equal episode counts can entail different numbers of transitions. For A3, match environment interactions, separate evaluation episodes from training, and examine seed-to-seed spread. The fixed-policy variance measured in B05 and the training performance plotted here answer different questions. [Book Fig. 13.2](../../../sources/RLbook2020.pdf#page=352)

### B07 · Advantage compares an action with the policy at that state · 6 min

Reuse P45’s advantage equation, updating its notation:
\[
A^\pi(s,a)=q^\pi(s,a)-v^\pi(s),\qquad
\mathbb E_\pi[G_t-v^\pi(S_t)\mid S_t=s,A_t=a]=A^\pi(s,a).
\]
Show the full fork. At θ = 0, reveal \(v^\pi(\mathrm{upper})=3,\ v^\pi(\mathrm{lower})=1\). Ask students to find the start action values, start value and right-action advantage. Reveal \(q^\pi(\mathrm{start},\mathrm{right})=3.5,\ q^\pi(\mathrm{start},\mathrm{left})=2.5,\ v^\pi(\mathrm{start})=3\). Right’s advantage is +0.5.

**Notes.** Start action values include the first reward 2 and half the expected final reward. The two exact advantages are +0.5 and −0.5; their policy-weighted mean is zero. On B01’s particular right–left episode the centered return at start is \(3-3=0\). An action with positive advantage can produce this sample. Returning to D07a, \(A^\pi\) can replace \(q^\pi\) in the same discounted sum because the subtracted state value is a baseline.

### B08 · Learn the baseline and update the policy · 6 min

Adapt P46 into two columns. Left: **Value fit**. Freeze the current predictions for use in the actor weights. Train \(\hat v(s,\mathbf w)\) by minimizing the mean of \(\tfrac12[G_t-\hat v(S_t,\mathbf w)]^2\). Right: **Actor update**. Use the frozen numbers in
\[
\hat A_t=G_t-\hat v(S_t,\mathbf w),\qquad
\boldsymbol\theta\leftarrow\boldsymbol\theta+
\alpha_{\boldsymbol\theta}\sum_t\gamma^t\hat A_t\,\nabla_{\boldsymbol\theta}\log\pi(A_t\mid S_t,\boldsymbol\theta).
\]
“Which quantity gets a gradient from each loss?”

**Notes.** For this update use baseline predictions from before this rollout was collected. Save those predictions, then fit the baseline to the returns for future rollouts using its own step size \(\alpha_{\mathbf w}\). The policy loss is the negative sum of \(\gamma^t\hat A_t\log\pi\); stop gradients through \(\hat A_t\). Differentiation of that loss changes the policy parameters. Separate value regression changes **w**. Simply detaching a prediction fitted to the very same sampled actions does not remove statistical dependence on those actions. The episode remains the sampling unit for averaging actor sums.

### B09 · Can the actor learn after one transition? · 6 min

Adapt P48’s question and the TD-error identity on P51. Use the start → upper transition. Highlight where the value prediction is used a second time:
\[
\delta_t=R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w)-\hat v(S_t,\mathbf w).
\]
Label current prediction “what was expected here” and successor prediction “how the sampled action’s continuation is judged.” Reveal: using the true state values gives \(\mathbb E_\pi[\delta_t\mid S_t=s,A_t=a]=A^\pi(s,a)\). Ask “Which prediction can depend on the action through the next state?”

**Notes.** The expected reward plus discounted true successor value gives \(q^\pi(s,a)\) by the Bellman equation. Subtract the state value to obtain the advantage. The actor can use \(\gamma^t\delta_t\nabla_{\boldsymbol\theta}\log\pi(A_t\mid S_t,\boldsymbol\theta)\) immediately. Set terminal value to zero. Second psychology cue: a prediction error measures how far the outcome departs from expectation; the same idea appears in models of conditioning. Approximation errors in the successor estimate can be systematically different after different actions. [Book §§13.5 and 14.2](../../../sources/RLbook2020.pdf#page=353)

### B10 · Can a critic reverse the update? · 6 min

Rebuild P59’s bias discussion on the fork. Give the critic predictions **start 3, upper 0, lower 3**. Students fill the last column before the reveal.

| First action | True action value | One-step target using this critic |
| --- | ---: | ---: |
| Right → upper | 3.5 | \(2+½(0)=2\) |
| Left → lower | 2.5 | \(2+½(3)=3.5\) |

Ask “Which first action does this critic favor?” Reveal **left**. Then display the whole-episode result, keeping the heading **expected update to the shared preference at θ = 0**: true gradient **+0.5**; using this critic **−0.125**. End with the 8.1 question: “After observing a transition, how should the critic learn and how should the actor use its judgment?”

**Notes.** Early predictions suffice for the error. The same current-state subtraction applies to both first actions. Exact first-decision contribution: \(½[(3.5-3)(+½)+(2.5-3)(-½)]=+0.25\). With the critic: \(½[(2-3)(+½)+(3.5-3)(-½)]=-0.375\). At the final decision the successor is terminal, so the error in the current branch value acts only as a state baseline. The expected final contribution, including the outer ½ discount, is +0.25 for either critic. Totals are +0.5 and −0.125. Keep the arithmetic supporting the second contribution in notes; students need only predict the changed ranking and explain where the error enters. This example motivates 8.1’s full update.

### ADM · Project formulation and design checkpoint · 5 min administration

Show “Bring a runnable environment or data pipeline, a simple baseline, one planned comparison, an evaluation protocol, and a compute budget with a fallback.” Use the balance of the slot for checkpoint questions. These minutes are separate from the 58 teaching minutes. [Project decisions, formulation/design](../../../decisions/project_decisions.md)
