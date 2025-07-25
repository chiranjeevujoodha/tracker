from django.shortcuts import render
from django.http import JsonResponse
from .models import workout_group, exercise, Workout_sessions
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
def home(request):
    groups = workout_group.objects.all()
    exercises = exercise.objects.all()
    sessions = Workout_sessions.objects.all()
    return render(request, 'app/home.html', {
        'groups': groups,
        'exercises': exercises,
        'sessions': sessions
        })


@csrf_exempt
def save_session_ajax(request):
    if request.method == "POST":
        group_ids = request.POST.getlist('workout_group')  # from multi-select
        session_date = request.POST.get('session_date')

        if not group_ids or not session_date:
            return JsonResponse({'status': 'error', 'message': 'Missing fields'}, status=400)
        
        # Save one session per group
        for gid in group_ids:
            Workout_sessions.objects.create(
                workout_group_id = gid,
                session_date=session_date
            )
        return JsonResponse({'status': 'success', 'message': 'Sessions saved successfully'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


def sessions_list(request):
    qs = (Workout_sessions.objects
          .select_related('workout_group')
          .order_by('-session_date', 'workout_group__group'))
    print("Sessions:", list(qs))

    data = [{
        "id": s.id,
        "date": s.session_date.strftime('%Y-%m-%d'),
        "group": s.workout_group.group
    } for s in qs]

    return JsonResponse({"sessions": data})

