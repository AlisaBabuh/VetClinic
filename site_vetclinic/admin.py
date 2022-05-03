from django.contrib import admin

from site_vetclinic.models import GroupService, Pet, PetType, MedicalCard, MedicalRecord, Speciality, Timetable, Service, Record, User, VetProfile

class PetAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pet, PetAdmin)

class PetTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(PetType, PetTypeAdmin)

class MedicalCardAdmin(admin.ModelAdmin):
    pass
admin.site.register(MedicalCard, MedicalCardAdmin)

class MedicalRecordAdmin(admin.ModelAdmin):
    pass
admin.site.register(MedicalRecord, MedicalRecordAdmin)

class VetProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(VetProfile, VetProfileAdmin)

class SpecialityAdmin(admin.ModelAdmin):
    pass
admin.site.register(Speciality, SpecialityAdmin)

class TimetableAdmin(admin.ModelAdmin):
    pass
admin.site.register(Timetable, TimetableAdmin)

class ServiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Service, ServiceAdmin)

class GroupServiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(GroupService, GroupServiceAdmin)

class RecordAdmin(admin.ModelAdmin):
    pass
admin.site.register(Record, RecordAdmin)

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)