# A1 starter

See the assignment handout for the tasks. Quick reference:

    python -m pip install -r requirements.txt
    pytest                                  # all public tests
    pytest tests/test_part1_planning.py     # one part
    pytest -k debug                         # only the 2 x 2 debugging cases
    python run_experiments.py               # writes results/

You edit `dp.py`, `prediction.py`, `control.py`, `answers.md` and `llm_report.md`.
Everything under `rlhw/`, `tests/`, `data/` and `run_experiments.py` is supplied;
grading uses clean copies of those files, so changes to them have no effect.
