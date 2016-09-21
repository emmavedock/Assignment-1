#a1test.py
#Emma Vedock-Gross ev225 Trey Aguirre tea42
#9/18/2016

"""Unit test for module a1
When run as a script, this module invokes several procedures that 
test the various functions in the module a1."""

import cornelltest
import a1

#need four test cases for each
#needs specification, test for part A
def testA():
    #test cases for before_space function
    result=a1.before_space('abc def')
    cornelltest.assert_equals('abc',result)
    
    result=a1.before_space(' abc def')
    cornelltest.assert_equals('',result)
    
    result=a1.before_space('ab cd ef')
    cornelltest.assert_equals('ab',result)
    
    result=a1.before_space('abc  def')
    cornelltest.assert_equals('abc',result)
    
    #test cases for after_space function
    result=a1.after_space('abc def')
    cornelltest.assert_equals('def',result)
    
    result=a1.after_space(' abc def')
    cornelltest.assert_equals('abc def',result)
    
    result=a1.after_space('ab cd ef')
    cornelltest.assert_equals('cd ef',result)
    
    result=a1.after_space('abc  def')
    cornelltest.assert_equals(' def',result)
    
    result=a1.after_space('abc def ')
    cornelltest.assert_equals('def ',result)
    

def testB():
    #test cases for first_inside_quotes
    result=a1.first_inside_quotes('a "bc" d')
    cornelltest.assert_equals('bc',result)
    
    result=a1.first_inside_quotes('"ab" c')
    cornelltest.assert_equals('ab',result)
    
    result=a1.first_inside_quotes('ab "cd" "de"')
    cornelltest.assert_equals('cd',result)
    
    result=a1.first_inside_quotes('ab"cd"')
    cornelltest.assert_equals('cd',result)
    
    #test cases for get_from
    result=a1.get_from('{ "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : true, "error" : "" }')
    cornelltest.assert_equals('2.5 United States Dollars',result)
    
    result=a1.get_from('{ "from" : "40 Chinese Yuan", "to" : "23.864622009701 Romanian Lei", "success" : true, "error" : "" }')
    cornelltest.assert_equals('40 Chinese Yuan',result)
    
    result=a1.get_from('{ "from" : "1000 Zimbabwean Dollars", "to" : "26.611461135503 Swedish Kronor", "success" : true, "error" : "" }')
    cornelltest.assert_equals('1000 Zimbabwean Dollars',result)
    
    result=a1.get_from('{ "from" : "80 Gibraltar Pounds", "to" : "2349.5741654147 Ethiopian Birr", "success" : true, "error" : "" }')
    cornelltest.assert_equals('80 Gibraltar Pounds',result)

    #test cases for get_to
    result=a1.get_to('{ "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : true, "error" : "" }')
    cornelltest.assert_equals('2.24075 Euros',result)
    
    result=a1.get_to('{ "from" : "40 Chinese Yuan", "to" : "23.864622009701 Romanian Lei", "success" : true, "error" : "" }')
    cornelltest.assert_equals('23.864622009701 Romanian Lei',result)
    
    result=a1.get_to('{ "from" : "1000 Zimbabwean Dollars", "to" : "26.611461135503 Swedish Kronor", "success" : true, "error" : "" }')
    cornelltest.assert_equals('26.611461135503 Swedish Kronor',result)
    
    result=a1.get_to('{ "from" : "80 Gibraltar Pounds", "to" : "2349.5741654147 Ethiopian Birr", "success" : true, "error" : "" }')
    cornelltest.assert_equals('2349.5741654147 Ethiopian Birr',result)
    
    #test cases for has_error
    result=a1.has_error('{ "from" : "", "to" : "", "success" : false, "error" : "Currency amount is invalid." }')
    cornelltest.assert_true(result)
    
    result=a1.has_error('{ "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : true, "error" : "" }')
    cornelltest.assert_false(result)
    
    result=a1.has_error('{ "from" : "", "to" : "", "success" : false, "error" : "Exchange currency code is invalid." }')
    cornelltest.assert_true(result)
    
    result=a1.has_error('{ "from" : "40 Chinese Yuan", "to" : "23.864622009701 Romanian Lei", "success" : true, "error" : "" }')
    cornelltest.assert_false(result)
    

def testC():
    #test procedures for currency_response function
    result = a1.currency_response('USD', 'EUR', 2.5)
    cornelltest.assert_equals('{ "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : true, "error" : "" }', result)
    
    result = a1.currency_response('CNY', 'RON', 40.0)
    cornelltest.assert_equals('{ "from" : "40 Chinese Yuan", "to" : "23.864622009701 Romanian Lei", "success" : true, "error" : "" }', result)
    
    result = a1.currency_response('ZWL', 'SEK', 1000.0)
    cornelltest.assert_equals('{ "from" : "1000 Zimbabwean Dollars", "to" : "26.611461135503 Swedish Kronor", "success" : true, "error" : "" }', result)
    
    result = a1.currency_response('GIP', 'ETB', 80.0)
    cornelltest.assert_equals('{ "from" : "80 Gibraltar Pounds", "to" : "2349.5741654147 Ethiopian Birr", "success" : true, "error" : "" }', result)


def testD():
    #test procedures for iscurrency function
    cornelltest.assert_true(a1.iscurrency('USD'))
    
    cornelltest.assert_false(a1.iscurrency('ZZZ'))
    
    cornelltest.assert_true(a1.iscurrency('SEK'))
    
    cornelltest.assert_false(a1.iscurrency('123'))
    
    #test procedures for exchange function
    result = a1.exchange('USD', 'EUR', 2.5)
    cornelltest.assert_floats_equal(2.24075, result)
    
    result = a1.exchange('CNY', 'RON', 40.0)
    cornelltest.assert_floats_equal(23.864622009701, result)
    
    result = a1.exchange('ZWL', 'SEK', 1000.0)
    cornelltest.assert_floats_equal(26.611461135503, result)
    
    result = a1.exchange('GIP', 'ETB', 80.0)
    cornelltest.assert_floats_equal(2349.5741654147, result)

testA()
testB()
testC()
testD()
    
print "Module a1 passed all tests."
