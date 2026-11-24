"""SDK 1.0 conformance (mlaify/AttackMap#254): attackmap.sdk.testing.assert_conforms."""

from pathlib import Path

from attackmap.sdk.testing import assert_conforms

from attackmap_analyzer_omeka_s import OmekaSAnalyzer


def _has_signals(result) -> None:
    assert any(isinstance(v, list) and v for v in result.__dict__.values()), "the analyzer emitted nothing"


FIXTURE = Path(__file__).parent / "fixtures" / "omeka_core_api"


def test_conforms_to_the_sdk() -> None:
    _has_signals(assert_conforms(OmekaSAnalyzer(), FIXTURE))
