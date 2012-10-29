from friendlib.views import get_search_context, get_user_context

class MediamisContextMiddleware(object):
    def process_request(self, request):
        pass

    def process_view(self, request, view_func, view_args, view_kwargs):
        """ Add extra context for all pages """

        # We don't touch the default pages ... (?)
        if view_func.__name__ == 'serve':
            return

        extra_context = self.get_extra_context(request)

        view_kwargs.update({'extra_context': extra_context})

    def process_template_response(self, request, response):
        extra_context = self.get_extra_context(request)
        response.context_data.update(extra_context)
        return response

    def get_extra_context(self, request):
        extra_context = {}

        # Context for searching
        search_args = request.GET or {}
        try:
            search_args.update({'owner': request.user.pk})
        except:
            # For proper search, it doesn't work
            pass
        search_context = get_search_context(search_args)

        # Context for logged user
        user_context = get_user_context(request.user)

        extra_context.update(search_context)
        extra_context.update(user_context)

        return extra_context

