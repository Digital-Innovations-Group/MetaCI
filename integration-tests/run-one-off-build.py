from os import environ
from unittest.mock import patch

import pytest

from metaci.build.management.commands._utils import make_build
from metaci.build.management.commands.run_build_from_id import Command
from metaci.conftest import (
    BranchFactory,
    OrgFactory,
    PlanFactory,
    PlanRepositoryFactory,
    RepositoryFactory,
    UserFactory,
)


@pytest.mark.django_db
@patch("metaci.build.tasks.reset_database_connection", lambda: ...)
class TestOneOffBuild:
    @patch.dict(environ, {"LOG_TO_STDERR": "True"})
    def test_one_off_build(self):
        repo = RepositoryFactory(
            name="CumulusCI-Test",
            owner="SFDO-Tooling",
            url="https://github.com/SFDO-Tooling/CumulusCI-Test",
        )
        OrgFactory(name="myorg", repo=repo, scratch=False)
        plan = PlanFactory(
            name="myplan",
            org="myorg",
            queue="long-running",
            flows="ci_test_concurrency",
        )
        BranchFactory(name="main", repo=repo)
        PlanRepositoryFactory(repo=repo, plan=plan)
        UserFactory(username="fake_username")
        build = make_build(
            "CumulusCI-Test",
            "main",
            "main",
            "myplan",
            "fake_username",
        )
        c = Command()
        c.handle(build_id=build.id)
