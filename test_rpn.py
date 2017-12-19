from rpn import RPNCalculator
import pytest
class TestRPN:
	
	def test_single_operator_addition(self):
		expersion='2,3,+'
		expected=5.0
		assert expected == RPNCalculator().evaluate(expersion)
		
	
	def test_single_operator_addition_no_operand(self):
		expersion='+'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)
	
	def test_single_operator_addition_one_operand(self):
		expersion='2,+'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_single_operator_addition_no_operator(self):
		expersion='2,3'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_addition(self):
		expersion='2,3,+,4,+'
		expected=9.0
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_addition_continuous_operator(self):
		expersion='2,3,4,+,+'
		expected=9.0
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_addition_no_operand(self):
		expersion='+,+'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_addition_multiple_operand(self):
		expersion='2,3,+,+'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operand_addition_no_operator(self):
		expersion='2,3,4'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_no_operand_addition_no_operator(self):
		expersion=''
		expected='Please enter some value'
		assert expected == RPNCalculator().evaluate(expersion)
	
	def test_only_separator(self):
		expersion=','
		expected='Please enter some value'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_separator(self):
		expersion=',,'
		expected='Please enter some value'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_addition_multiple_operand_comma_at_last(self):
		expersion='2,3,+,+,'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_addition_continuous_operator_comma_at_last(self):
		expersion='2,3,4,+,+,'
		expected=9.0
		assert expected == RPNCalculator().evaluate(expersion)

	def test_single_operator_sub(self):
		expersion='2,3,-'
		expected=-1.0
		assert expected == RPNCalculator().evaluate(expersion)
		
	
	def test_single_operator_sub_no_operand(self):
		expersion='-'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)
	
	def test_single_operator_sub_one_operand(self):
		expersion='2,-'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_single_operator_sub_no_operator(self):
		expersion='2,3'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_sub(self):
		expersion='2,3,-,4,-'
		expected=-5.0
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_sub_continuous_operator(self):
		expersion='2.0,3.2,4,-,-'
		expected=2.8
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_sub_no_operand(self):
		expersion='-,-'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_sub_multiple_operand(self):
		expersion='2,3,-,-'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operand_sub_no_operator(self):
		expersion='2,3,4'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_no_operand_sub_no_operator(self):
		expersion=''
		expected='Please enter some value'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_only_separator(self):
		expersion=','
		expected='Please enter some value'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_separator(self):
		expersion=',,'
		expected='Please enter some value'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_sub_multiple_operand_comma_at_last(self):
		expersion='2,3,-,-,'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_sub_continuous_operator_comma_at_last(self):
		expersion='2,3,4,-,-,'
		expected=3.0
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_sub_continuous_operator_one_alphabet(self):
		expersion='2,3,4,-,-,A'
		expected=3.0
		assert expected == RPNCalculator().evaluate(expersion)

	def test_only_alphabet(self):
		expersion='A'
		expected="Please enter some value"
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_sub_add_continuous_operator(self):
		expersion='2,3,4,-,+'
		expected=1.0
		assert expected == RPNCalculator().evaluate(expersion)

	def test_single_operator_mul(self):
		expersion='2,3,*'
		expected=6.0
		assert expected == RPNCalculator().evaluate(expersion)
		
	
	def test_single_operator_mul_no_operand(self):
		expersion='*'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)
	
	def test_single_operator_mul_one_operand(self):
		expersion='2,*'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_single_operator_mul_no_operator(self):
		expersion='2,3'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_mul(self):
		expersion='2,3,*,4,*'
		expected=24.0
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_mul_continuous_operator(self):
		expersion='2,3,4,*,*'
		expected=24.0
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_mul_no_operand(self):
		expersion='*,*'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_mul_multiple_operand(self):
		expersion='2,3,*,*'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operand_mul_no_operator(self):
		expersion='2,3,4'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	
	def test_multiple_operator_mul_multiple_operand_comma_at_last(self):
		expersion='2,3,*,*,'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_mul_continuous_operator_comma_at_last(self):
		expersion='2,3,4,*,*,'
		expected=24.0
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operator_sub_add_mul_continuous_operator(self):
		expersion='2,3,*,4,-,5,+'
		expected=7.0
		assert expected == RPNCalculator().evaluate(expersion)

	def test_single_operator_div(self):
		expersion='2,3,/'
		expected=0.7
		assert expected == RPNCalculator().evaluate(expersion)
		
	
	def test_single_operator_div_no_operand(self):
		expersion='/'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)
	
	def test_single_operator_div_one_operand(self):
		expersion='2,/'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_single_operator_div_no_operator(self):
		expersion='2,3'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_divtiple_operator_div(self):
		expersion='2,3,/,4,/'
		expected=0.2
		assert expected == RPNCalculator().evaluate(expersion)

	def test_divtiple_operator_div_continuous_operator(self):
		expersion='2,3,4,/,/'
		expected=2.7
		assert expected == RPNCalculator().evaluate(expersion)

	def test_divtiple_operator_div_no_operand(self):
		expersion='/,/'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_divtiple_operator_div_divtiple_operand(self):
		expersion='2,3,/,/'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_divtiple_operand_div_no_operator(self):
		expersion='2,3,4'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	
	def test_divtiple_operator_div_divtiple_operand_comma_at_last(self):
		expersion='2,3,/,/,'
		expected='Error'
		assert expected == RPNCalculator().evaluate(expersion)

	def test_divtiple_operator_div_continuous_operator_comma_at_last(self):
		expersion='2,3,4,/,/,'
		expected=2.7
		assert expected == RPNCalculator().evaluate(expersion)

	def test_divtiple_operator_sub_add_mul_div_continuous_operator(self):
		expersion='2,3,/,4,-,5,+,6,*'
		expected=10.0
		assert expected == RPNCalculator().evaluate(expersion)
	def test_single_operand_percent(self):
		expersion='20,%'
		expected=0.2
		assert expected == RPNCalculator().evaluate(expersion)

	def test_multiple_operand_percent(self):
		expersion='2,3,+,5,*,4,-,%'
		expected=0.2
		assert expected == RPNCalculator().evaluate(expersion)
#		raise





tes tekndlkwnd epfnwef w f qlkqwn;qnr
