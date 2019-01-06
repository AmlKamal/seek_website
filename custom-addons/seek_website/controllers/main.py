# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class seek(http.Controller):

#all jobs contoller 
	@http.route('/seek', auth='public', website=True)
	def jobs(self, **kwargs):
		seekjobs = request.env['seek.job']
		jobs = seekjobs.search([])
		return request.render('seek_website.seek',{'jobs':jobs})

#job details contoller 
	@http.route('/seek/<model("seek.job"):job>', auth='public',website=True)
	def detail(self, job, **kwargs):
		return http.request.render('seek_website.detail',{'job':job})

#apply for job contoller 
	@http.route('/apply_for_job_controller/<model("seek.job"):job>', type='http', auth='public', website=True , csrf=False) 
	def my_controller_method(self, **post):
		print(post)
		print(request.params)
		# apply=request.env['seek.application'].sudo().create({
		# 	'app_name' : request.params["name"],
   		# 	'app_phone_number': request.params["app_phone_number"],
    	# 	'app_email_address':request.params["app_email_address"],
    	# 	'app_nationality':request.params["app_nationality"],
    	# 	'app_cv':request.params["app_cv"],
		# })
		return http.request.render('seek_website.applicationform')
            # 'company_id': request.params["company_name"],
            # 'card_id': request.params["card_value"],
            # 'qty': request.params["qty"],
            # })
        # print(purchase_proces)
        # return purchase_proces

#submit application contoller
	@http.route('/application/submit', auth='public',website=True)
	def submit_job_application(self, **kwargs):
		# print(job)
		return http.request.render('seek_website.application_successful_message')


#Seeker profile contoller
	@http.route('/profile', auth='public', website=True)
	def profile(self, **kwargs):
		seeker = request.env['res.partner'].search([('partner_id','=',self.env.user.id)])
		return request.render('seek_website.profile',{'seeker':seeker})














       
	# @http.route('/profile/<model("seek.seeker"):seeker>', auth='public',website=True)
	# def profile(self, seeker, **kwargs):
	# 	return http.request.render('seek_website.profile',{'seeker':seeker})


	#Application
	# @http.route('/applicationform', website=True)
	# def apply(self, **kwargs):
	# 	return request.render('seek_website.applicationform')	


	# @http.route('/apply', website=True)
	# def apply(self, **kwargs):
	# 	job_types = [('employee', "Employee"), 
	# 				('volunteer', "Volunteer"),
	# 				('internship', "Internship"),
	# 				('contract', "Contract")]

	# 	return request.render('seek_website.apply',{'jobtypes':job_types,'jobsalarys':job_salarys})
	# 	return request.render('seek_website.apply',{'job_types':job_types})

	# @http.route('/apply', website=True)
	# def apply(self, **kwargs):
	# 	jobsalarys = request.env['seek.job'].search([])
	# 	return request.render('seek_website.apply',{'jobsalarys':jobsalarys})

	# @http.route('/apply', website=True)
	# def apply(self, **kwargs):
	# 	job_salarys = [('two_to_five', "2000-5000 SDG"), 
   	#  	('five_to_ten', "5000-10000 SDG"),
    # 	('ten_to_fifteen', "10000-15000 SDG"),
    # 	('more_than_fifteen', "15000+ SDG")]
	# 	return request.render('seek_website.apply',{'jobsalarys':job_salarys})

	# @http.route('/apply', website=True)
	# def apply(self, **kwargs):
	# 	jobstatus = request.env['seek.job'].search([])
	# 	return request.render(
	# 		'seek_website.apply',{'jobstatus':jobstatus})