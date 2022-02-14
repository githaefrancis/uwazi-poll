from . import admin

@admin.route('/admin')
def admin():
  return 'hello admin'