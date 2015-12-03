from __future__ import unicode_literals
import frappe
from frappe.utils import cstr,now,add_days
import json

@frappe.whitelist()
def get_support_ticket_data(args):
	"""
		args:{
			status: All, Closed, Open, Pending,
			start: val
			end: val
		}
		Support Ticket Data in following format
		{
			"lable":"Issue Status"
			"data": [["date","Issue 1"], ...,["date","Issue N"]]
		}
	"""
	# frappe.errprint(args)
	return [{
				"label":"Open",
				"data": [[1999, 3.0], [2000, 3.9], [2001, 2.0], [2002, 1.2], [2003, 1.3]]
			},
			{
				"label":"Close",
				"data": [[1999, 2.0], [2000, 2.9], [2001, 1.0], [2002, 3.2], [2003, 5.3]]
			},
			{
				"label":"Pending",
				"data": [[1999, 3.9], [2000, 10], [2001, 3.0], [2002, 2.2], [2003, 1.9]]
			}]
	pass

@frappe.whitelist()
def get_sample_data():
	return {
	"get_sample_data": frappe.db.sql("""select false, name, customer, type from `tabSample Entry Register`  order by name""", as_list=1)
	}

@frappe.whitelist()
def get_test_data(test_group):
	return {
	"get_test_data": frappe.db.sql("""select name from `tabTest Name` where test_group='%s' order by name"""%(test_group), as_list=1)
	}

@frappe.whitelist()
def create_job_card(test_group):
	frappe.msgprint("Job Card created successfuly for : "+test_group);

@frappe.whitelist()
def create_job_card_1(test_group,selectedData,test_list_unicode):
	print test_list_unicode
	test_list=json.loads(test_list_unicode)
	# for test in test_list:
	# 	frappe.msgprint("test is: "+ test)
	# frappe.msgprint(test_list[0])

	# bank=frappe.new_doc("Job Card Creation")
	# bank.sample_id = "SER0005"
	# bank.customer = "c"
	# bank.type = "Mineral Oil"
	# bank.save()
	# print type(selectedData)
	# frappe.msgprint("Job Card "+bank.name+" created successfuly for : "+test_group);
	#frappe.msgprint(type(selectedData))
	# print a
	# frappe.msgprint(len(selectedData))
	selectedData_json = json.loads(selectedData)
	for r in selectedData_json:
		doc_job_card_creation=frappe.new_doc("Job Card Creation")
		doc_job_card_creation.sample_id = r.get("sampleid")
		doc_job_card_creation.customer = r.get("customer")
		doc_job_card_creation.type = r.get("type")
		for test in test_list:
			test_req={
				"doctype": "Job Card Creation Test Details",
				"test_group": test_group,
				"test": test
			}
			doc_job_card_creation.append("test_details",test_req)
		doc_job_card_creation.save()
		frappe.msgprint("Job Card "+doc_job_card_creation.name+" is created successfuly for sample : "+r.get("sampleid"));
		# frappe.msgprint(r.get("sampleid")+r.get("type")+"customer "+r.get("customer"))


