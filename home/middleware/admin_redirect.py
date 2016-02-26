from django.http import HttpResponseRedirect
from django.conf import settings

class AdminRedirectMiddleware:
	""" allows you to customize redirects with the GET line in the admin """

	def process_response(self, request, response):
		# save redirects if given
		if request.method == "GET" and request.GET.get("next", False):
			request.session["next"] = request.GET.get("next")
		if settings.ADMIN_LOGIN_REDIRECT_URL and request.GET.get("next", '') == '/admin/':
			request.session["next"] = settings.ADMIN_LOGIN_REDIRECT_URL

		print ('===> ' + request.session.get("next", ''))

		# apply redirects
		if request.session.get("next", False) and \
		type(response) == HttpResponseRedirect and \
		request.path.startswith("/admin/"):
			path = request.session.get("next")
			del request.session["next"]
			print ('  path ===> ' + path)
			return HttpResponseRedirect(path)
		return response