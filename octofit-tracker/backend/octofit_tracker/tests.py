from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', username='testuser', team=team)
        self.assertEqual(str(user), 'testuser')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', username='testuser', team=team)
        activity = Activity.objects.create(user=user, activity_type='run', duration=30, date='2025-12-24')
        self.assertEqual(str(activity), 'testuser - run')

    def test_workout_creation(self):
        team = Team.objects.create(name='Test Team')
        workout = Workout.objects.create(name='Pushups')
        workout.suggested_for.add(team)
        self.assertEqual(str(workout), 'Pushups')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, total_points=100)
        self.assertEqual(str(leaderboard), 'Leaderboard for Test Team')
