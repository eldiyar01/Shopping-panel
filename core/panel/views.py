from django.shortcuts import render, redirect

from .models import Date, Product


def home(request):
    dates = Date.objects.all()
    return render(request, 'panel/home.html', {"dates": dates})


def sorter(request):
    dates = Date.objects.all()
    print(request)
    return render(request, 'panel/home.html', {"dates": dates})




# def university_dtl(request, pk):
#     university = University.objects.get(id=pk)
#     return render(request, 'university/details.html', {'university': university})
#
#
# def fast_search(request):
#     search_req = request.GET.get('search')
#     search_univ = search_req
#     if search_req == '':
#         return redirect('university:home')
#     elif search_req:
#         search_univ = University.objects.filter(title__icontains=search_req)
#     return render(request, 'university/search_res.html', {'search_univ': search_univ, 'search_req': search_req})
#
#
# def searcher(request):
#     return render(request, 'university/searcher.html',)
#
#
# def searcher_res(request):
#     search_req = request.GET.dict()
#     degree = search_req.get('degree')
#     faculty = search_req.get('faculty')
#     language = search_req.get('language')
#     basis = search_req.get('basis')
#     aid = search_req.get('aid')
#     scholarship = search_req.get('scholarship')
#     if basis == 'budget':
#         fee = 0
#         search_req['fee'] = 0
#     else:
#         fee = search_req.get('fee')
#     if scholarship is None:
#         scholarship = False
#     if aid is None:
#         aid = False
#     f_id = Faculty.objects.filter(title__icontains=faculty, language__icontains=language[:2],
#                                   fee__range=(1, fee), aid=aid, scholarship=scholarship).values_list('id', flat=True)
#     search_univ = f_id
#     if search_req == '':
#         return redirect('university:home')
#     elif search_req:
#         search_univ = Degree.objects.filter(qualifications__icontains=degree, faculties__in=list(f_id))
#     return render(request, 'university/search_res.html', {'searcher_res': search_univ, 'searcher_req': search_req})
#
#
# def features(request):
#     return render(request, 'features/soon.html')
#
#
# def team(request):
#     return render(request, 'about/team.html')
