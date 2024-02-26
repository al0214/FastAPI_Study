package org.example.calculator.calculate;

public interface NewArithmeticOperator {
    boolean supports(String operator);
    int calculator(PositiveNumber operand1, PositiveNumber operand2);
}
