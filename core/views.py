from django.views.generic import TemplateView


class IdeaDashboardView(TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['ideas'] = [
            {
                'title': 'Smart Study Planner',
                'problem': 'Students struggle to organize tasks before deadlines.',
                'solution': 'AI-based daily planning with reminders and focus sessions.',
                'impact': 'Improves productivity and reduces last-minute stress.'
            },
            {
                'title': 'Campus Help Desk',
                'problem': 'Students do not know where to ask quick questions.',
                'solution': 'A central assistant that answers common FAQs with live support.',
                'impact': 'Saves time for both students and staff.'
            },
            {
                'title': 'Local Event Finder',
                'problem': 'Students miss events due to scattered information.',
                'solution': 'A one-stop dashboard for college events, clubs, and workshops.',
                'impact': 'Increases student participation and engagement.'
            },
        ]

        return context
