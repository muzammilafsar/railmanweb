from django import forms

class LiveTrain(forms.Form):
    train_no = forms.IntegerField(label='train_no')

class PnrForm(forms.Form):
    pnr_no=forms.IntegerField(label='pnr_no')