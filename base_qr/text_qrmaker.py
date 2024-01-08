import qrcode

project_dir = project.folder
file_name = 'test.png'
file_path = '{}/{}'.format(project_dir, file_name)
qr_data = op('table_qr_data')[0,0].val
new_img = qrcode.make(qr_data)

new_img.save(file_path)
op('moviefilein1').par.file = file_path
op('moviefilein1').par.reloadpulse.pulse()