from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def custom_404(request, exception):
    return render(request, "404.html", {
        "request_path": request.path}, status=404
    )


def custom_500(request):
    return render(request, "500.html", status=500)


def custom_400(request, exception):
    return render(request, "400.html", status=400)


def custom_403(request, exception):
    return render(request, "403.html", status=403)
