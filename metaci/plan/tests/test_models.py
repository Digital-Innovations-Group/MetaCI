from django.test import TestCase

from metaci.plan.models import Plan
from metaci.repository.models import Repository


class PlanTestCase(TestCase):
    def setUp(self):
        self.repo = Repository(
            name="TestRepo",
            owner="TestOwner",
            url="https://github.com/TestOwner/TestRepo",
        )
        self.commit_plan = Plan(
            name="Test Plan",
            role="feature",
            trigger="commit",
            regex="test/.*",
            flows="test_flow",
            org="test_org",
            context="test case",
        )
        self.tag_plan = Plan(
            name="Test Plan",
            role="feature",
            trigger="tag",
            regex="test/.*",
            flows="test_flow",
            org="test_org",
            context="test case",
        )

    def test_check_github_event__commit_matches(self):
        payload = {"ref": "refs/heads/test/matches", "after": "0123456789"}
        run_build, commit, commit_message = self.commit_plan.check_github_event(
            "push", payload
        )
        self.assertTrue(run_build)
        self.assertEqual(commit, payload["after"])

    def test_check_github_event__commit_does_not_match(self):
        payload = {"ref": "refs/heads/no-match"}
        run_build, commit, commit_message = self.commit_plan.check_github_event(
            "push", payload
        )
        self.assertFalse(run_build)
        self.assertEqual(commit, None)

    def test_check_github_event__commit_tag_event(self):
        payload = {"ref": "refs/tags/test/matches", "head_commit": None}
        run_build, commit, commit_message = self.commit_plan.check_github_event(
            "push", payload
        )
        self.assertFalse(run_build)
        self.assertEqual(commit, None)

    def test_check_github_event__tag_matches(self):
        payload = {"ref": "refs/tags/test/matches", "head_commit": {"id": "0123456789"}}
        run_build, commit, commit_message = self.tag_plan.check_github_event(
            "push", payload
        )
        self.assertTrue(run_build)
        self.assertEqual(commit, payload["head_commit"]["id"])

    def test_check_github_event__tag_does_not_match(self):
        payload = {"ref": "refs/tags/no-match", "head_commit": None}
        run_build, commit, commit_message = self.tag_plan.check_github_event(
            "push", payload
        )
        self.assertFalse(run_build)
        self.assertEqual(commit, None)

    def test_check_github_event__tag_commit_event(self):
        payload = {"ref": "refs/heads/test/matches", "head_commit": None}
        run_build, commit, commit_message = self.tag_plan.check_github_event(
            "push", payload
        )
        self.assertFalse(run_build)
        self.assertEqual(commit, None)
