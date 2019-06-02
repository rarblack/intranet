from django.contrib import admin
from .models import WorkPlace, Employee, EmployeeInstance, Company, Transportation, Profession


class EmployeeInstanceInline(admin.TabularInline):
    model = EmployeeInstance


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    display = 'profession_name'


@admin.register(Transportation)
class EvacuationPlanAdmin(admin.ModelAdmin):
    display = 'transport_name'


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    display = 'company_name'


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'status')
    inline = [EmployeeInstanceInline]


@admin.register(EmployeeInstance)
class EmployeeInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'employee', 'work_place', 'start_time', 'end_time', 'is_terminated')
    list_filter = ('user', 'work_place')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'account', None) is None:
            obj.account.user = request.user
        obj.save()


# @admin.register(Log)
# class LogAdmin(admin.ModelAdmin):
#     list_display = ('employee_instance', 'related_id')
#     list_filter = ('editor', 'related_id', 'is_changed',)
#     fieldsets = (
#         ('Details', {
#             'fields': ('id', 'editor',)
#         }),
#         ('Flags', {
#             'fields': ('is_terminated',)
#         }),
#     )


admin.site.register(WorkPlace)
