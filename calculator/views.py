# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def calculator(request):
    # Creates a context dictionary (map) to send data to the templated HTML file
    context = {}

    # Retrieve the 'name' parameter, if present, and add it to the context
    if not 'display_number' in request.POST:
    	context['display_number'] = "0"
    	context['opr'] = "+"
    	context['prev_number'] = "0"

    	
    else:
    	context['display_number'] = request.POST['display_number']
    	context['opr'] = request.POST['opr']
    	context['prev_number'] = request.POST['prev_number']
    	context['new_number'] = request.POST['new_number']

    # number-button clicked
    if 'btn_num' in request.POST:
        context['new'] = request.POST['btn_num']
        if context['new'].isdigit():
        	if context['opr'] != "":
        		context['new_number'] = int(str(context['new_number'])+str(context['new']))
        		context['display_number'] = context['new_number']
        		print("HERE")
        		return render(request, 'calculator/calculator.html', context)

        	else:
        		context['prev_number'] = int(str(context['prev_number']) + str(context['new']))
        		context['display_number'] = context['prev_number']
        		return render(request, 'calculator/calculator.html', context)

        else:
        	context["msg"] = "Hey, don't change the button value :-) "
        	return render(request, 'calculator/calculator.html', context)


    # operator-button clicked
    else:
    	if 'btn_opr' in request.POST:
    		# print("1: ", request.POST['btn_opr'])
    		
    		if context['opr'] == "":
    			context['opr'] = request.POST['btn_opr']
    			# return render(request, 'calculator/calculator.html', context)
    			

    		elif context['opr'] != "":
    			if context['opr'] == "=":
    		 		context['prev_number'] = context['new_number']
    				# print("EQUALS", context['prev_number'], context['new_number'], context['opr'])
    				

    			else:
    				try:
    					if context['opr'] == "+":
    						context['prev_number'] = int(context['prev_number'])+int(context['new_number'])
    						# print('PLUS', context['prev_number'])
	
	    				elif context['opr'] == "-":
	    					 context['prev_number'] = int(context['prev_number'])-int(context['new_number'])
	
	    				elif context['opr'] == "*":
	    					 context['prev_number'] = int(context['prev_number'])*int(context['new_number'])
	
	    				elif context['opr'] == "/":
	    					# exception 01 : divide by zero
	    					if context['new_number'] == "0":
	    						context["msg"] = "Hey, don't divide by ZERO :-( "
	    						context['prev_number'] = "0"
	        	
	    					else:
    							context['prev_number'] = int(context['prev_number'])/int(context['new_number'])
    				
    				# exception 02 : double-click operators
    				except ValueError:
    						context["msg"] = "Hey, don't double-click operators! :-( "
    						context['prev_number'] = "0"
    						# print("EXCEPTION", context['prev_number'], context['new_number'], context['opr'])
    						return render(request, 'calculator/calculator.html', context)


    			context['opr'] = request.POST['btn_opr']
    			context['new_number'] = ""
    			print(context['opr'])
    			context['display_number'] = context['prev_number']
    			# return render(request, 'calculator/calculator.html', context)


    	return render(request, 'calculator/calculator.html', context)
    



