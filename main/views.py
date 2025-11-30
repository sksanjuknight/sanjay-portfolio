"""
Views for the portfolio application.
"""
from django.views.generic import TemplateView


class PortfolioView(TemplateView):
    """
    Class-based view to render the portfolio homepage.
    This is a static single-page application with no database queries.
    """
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        """
        Provide context data for the template.
        This could include dynamic data if needed in the future.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sanjay Rangreji - Portfolio'
        context['description'] = 'BCA Graduate | Python & Django Developer | Data Enthusiast'
        return context
