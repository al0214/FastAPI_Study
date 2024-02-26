package org.example;

public class WrongPasswordGenerator implements PasswordGenerator{
    @Override
    public String generatePassword() {
        return "as"; // 82글자
    }
}
