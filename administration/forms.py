from django import forms

from .models import (
   Empresa, 
   Regional,
   SubEstacion,
   Alimentadora,
   Transformador,
)



class EmpresaCreationForm(forms.ModelForm):

   direccion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': "3"}))

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for form in self.visible_fields():
         form.field.widget.attrs['class'] = 'form-control'

   class Meta:
      model = Empresa
      fields = ['nombre', 'direccion',]


class RegionalForm(forms.ModelForm):

   dia_lectura = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
   horario_lectura = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control'}))

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for form in self.visible_fields():
         form.field.widget.attrs['class'] = 'form-control'

   class Meta:
      model = Regional
      fields = ('empresa', 'nombre', 'dia_lectura', 'horario_lectura',)


class SubEstacionForm(forms.ModelForm):

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for form in self.visible_fields():
         form.field.widget.attrs['class'] = 'form-control'

   class Meta:
      model = SubEstacion
      fields = ('regional', 'nombre', 'capacidad',)


class AlimentadoraForm(forms.ModelForm):

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for form in self.visible_fields():
         form.field.widget.attrs['class'] = 'form-control'

   class Meta:
      model = Alimentadora
      fields = ('regional', 'sub_estaciones', 'nombre', 'descripcion',)


class TransformadorForm(forms.ModelForm):

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for form in self.visible_fields():
         form.field.widget.attrs['class'] = 'form-control'

   class Meta:
      model = Transformador
      fields = (
      'regional', 'sub_estaciones', 
      'alimentadora', 'marca', 'codigo', 
      'kva', 'medidor',
   )
