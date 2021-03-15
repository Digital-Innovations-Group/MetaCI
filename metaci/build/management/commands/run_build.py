from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from ._utils import do_build, make_build

User = get_user_model()


class Command(BaseCommand):
    help = "Runs a build from the command line (on local computer)."

    def add_arguments(self, parser):
        parser.add_argument("repo_name", type=str)
        parser.add_argument("branch_name", type=str)
        parser.add_argument("plan_name", type=str)
        parser.add_argument("commit", type=str)
        parser.add_argument("username_or_email", type=str)
        parser.add_argument(
            "--no-lock",
            action="store_true",
            help="Do not lock the org. Use with extreme caution.",
        )
        parser.add_argument(
            "--should-queue",
            action="store_true",
            help="Put it in the Plan's appropriate queue instead of running it immediately.",
        )

    def handle(
        self,
        repo_name,
        branch_name,
        commit,
        plan_name,
        username_or_email,
        *args,
        **options,
    ):
        build = make_build(
            repo_name,
            branch_name,
            commit,
            plan_name,
            username_or_email,
        )
        print("Running build", build)
        rc = do_build(build.id, options["no_lock"])
        print("Build finished", rc)
