from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data in correct order and individually
        for model in [Activity, Workout, Leaderboard, User, Team]:
            for obj in model.objects.all():
                obj.delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        users = [
            User.objects.create(email='ironman@marvel.com', username='Iron Man', team=marvel),
            User.objects.create(email='captain@marvel.com', username='Captain America', team=marvel),
            User.objects.create(email='spiderman@marvel.com', username='Spider-Man', team=marvel),
            User.objects.create(email='batman@dc.com', username='Batman', team=dc),
            User.objects.create(email='superman@dc.com', username='Superman', team=dc),
            User.objects.create(email='wonderwoman@dc.com', username='Wonder Woman', team=dc),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], activity_type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], activity_type='cycle', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[3], activity_type='swim', duration=60, date=timezone.now().date())

        # Create Workouts
        w1 = Workout.objects.create(name='Pushups', description='Upper body workout')
        w2 = Workout.objects.create(name='Squats', description='Lower body workout')
        w1.suggested_for.add(marvel)
        w2.suggested_for.add(dc)

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, total_points=150)
        Leaderboard.objects.create(team=dc, total_points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
