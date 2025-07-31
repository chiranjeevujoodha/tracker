from django.shortcuts import render
from django.http import JsonResponse
from .models import workout_group, exercise, Workout_sessions
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.dateparse import parse_date

# Create your views here.
def home(request):
    groups = workout_group.objects.all()
    exercises = exercise.objects.all()
    sessions = Workout_sessions.objects.select_related('workout_group').order_by('-session_date')
    return render(request, 'app/home.html', {
        'groups': groups,
        'exercises': exercises,
        'sessions': sessions
        })


def create_session(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            group_ids = data.get('workout_group', [])
            session_date = parse_date(data.get('session_date'))

            created_sessions = []

            for group_id in group_ids:
                group = workout_group.objects.get(id=group_id)
                session = Workout_sessions.objects.create(workout_group=group, session_date=session_date)
                created_sessions.append({
                    'date': session.session_date.strftime('%Y-%m-%d'),
                    'group': group.group
                })

            return JsonResponse({'status': 'success', 'sessions': created_sessions})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

