"""Offline checks for local studio plans."""
import unittest
from unittest.mock import patch

import studio_plans


class LocalStudio(unittest.TestCase):
    def setUp(self):
        self.words=[{"text":text,"start":i,"end":i+.8} for i,text in enumerate(
            ["The","first","scene.","Um","costs","25!","They","tried","again.","Then","it","worked."])]
    def test_filler_preserves_surrounding_audio(self):
        cuts=studio_plans.dialogue_plan(self.words,0,12,"filler","")
        self.assertEqual(cuts,[{"start":0,"end":3},{"start":3.8,"end":12}])
    def test_beats_are_bounded(self):
        cuts=studio_plans.dialogue_plan(self.words,0,12,"beats","")
        self.assertTrue(any(c.get("cue") and c["zoom"]>1 for c in cuts))
        self.assertAlmostEqual(sum(c["end"]-c["start"] for c in cuts),12)
    def test_ai_effects_only_reference_selected_passages(self):
        with patch.object(studio_plans.smart,"_model",return_value="local"),patch.object(studio_plans.llm,"complete",return_value='{"indices":[0],"broll_indices":[0],"zoom_indices":[0]}'):
            rows=studio_plans.dialogue_plan(self.words,0,12,"edit","zoom","stock")
        self.assertEqual(rows[0]["broll"],"stock")
        self.assertEqual(rows[0]["zoom"],1.14)
    def test_model_cannot_select_unknown_passage(self):
        with patch.object(studio_plans.smart,"_model",return_value="local"),patch.object(studio_plans.llm,"complete",return_value='{"indices":[99]}'):
            with self.assertRaises(ValueError):studio_plans.dialogue_plan(self.words,0,12,"recap","")
    def test_no_resolution_in_trailer_candidate_pool(self):
        with patch.object(studio_plans.smart,"_model",return_value="local"),patch.object(studio_plans.llm,"complete",return_value='{"indices":[0]}') as model:
            studio_plans.dialogue_plan(self.words,0,12,"trailer","")
        self.assertNotIn('worked.',model.call_args.args[1]['prompt'])
