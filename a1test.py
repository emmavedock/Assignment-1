#a1test.py
#Emma Vedock-Gross ev225
#9/8/2016

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
    
    
def testB():
    pass

def testC():
    pass

def testD():
    pass
#result = module.function()
#cornelltest.assert_equals('",result)

testA()
testB()
testC()
testD()
    
print "Module a1 passed all tests"