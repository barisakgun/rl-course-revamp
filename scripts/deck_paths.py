"""Keep generated deck candidates separate from instructor-editable PowerPoints."""
from pathlib import Path


def candidate_output(root, requested):
    """Use the spec's name only; its course/ destination cannot authorize overwrite."""
    root = Path(root).resolve()
    name = Path(requested).stem.removesuffix('.candidate') + '.candidate.pptx'
    result = root / 'output/deck_candidates' / name
    validate_candidate_output(root, result)
    return result


def validate_candidate_output(root, destination):
    root, destination = Path(root).resolve(), Path(destination)
    if not destination.resolve().is_relative_to(root / 'output'):
        raise ValueError('Generated decks must stay under output/, outside instructor-editable course/.')
    if not destination.name.endswith('.candidate.pptx'):
        raise ValueError('Generated decks must use the .candidate.pptx suffix.')
    if destination.exists():
        raise FileExistsError(f'Candidate already exists; preserve or remove it explicitly before rebuilding: {destination}')
