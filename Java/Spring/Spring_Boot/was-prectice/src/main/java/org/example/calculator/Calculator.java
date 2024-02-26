package org.example.calculator;


import org.example.calculator.calculate.*;

import java.util.List;



public class Calculator {
    private static final List<NewArithmeticOperator> arithmeticOperators = List.of(
            new AdditionOperator(),
            new SubtractionOperator(),
            new MultiplicationOperator(),
            new DivisionOperator());
    public static int arithmeticCalculate(PositiveNumber operand1, String operator, PositiveNumber operand2){
        return arithmeticOperators.stream().filter(arithmeticOperators -> arithmeticOperators.supports(operator))
                .map(arithmeticOperators -> arithmeticOperators.calculator(operand1,operand2))
                .findFirst()
                .orElseThrow(()->new IllegalArgumentException("올바른 사칙 연산이 아닙니다."));
    }
}
