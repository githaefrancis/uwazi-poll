from flask import redirect, render_template,request
from . import admin
from .forms import ElectionForm
from ..models import Election
from datetime import datetime


@admin.route('/admin',methods=['GET','POST'])
def admin():
  election_form=ElectionForm()
  elections=Election.query.order_by(Election.id.desc()).all()
  if request.method=='POST':
    if election_form.validate_on_submit():
      election_title=election_form.title.data
      start_time=election_form.start_time.data
      end_time=election_form.end_time.data
      date_time_obj=datetime.strptime(str(end_time), '%Y-%m-%d %H:%M:%S')
      new_election=Election(title=election_title,start_time=start_time,end_time=date_time_obj)
      new_election.save_election()
      return redirect(request.referrer)

  return render_template('admin/admin.html',election_form=election_form,elections=elections)
