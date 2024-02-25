package org.example;

import java.util.List;

public class GradeCalculator {
    private final Courses courses;


    public GradeCalculator(List<Course> courses) {
        this.courses = new Courses(courses);
    }

    public GradeCalculator(Courses courses){
        this.courses = courses;
    }

    /*
     * 요구 사항
     * 평균 학점 계산 방법 = (학점 수 * 교과목 평점)의 합계 / 수강 신청 총 학점 수
     * 일급 컬렉션 사용
     * */
    public double calculateGrade() {
//        (학점 수 * 교과목 평점)의 합계
        double totalMultipliedCreditAndCourseGrade = courses.multiplyCreditAndCourseGrade();


        // 수강 신청 총 학점 수
        int totalCompletedCredit = courses.calculateTotalCompletedCredit();

        return totalMultipliedCreditAndCourseGrade / totalCompletedCredit;
    }
}
