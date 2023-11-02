package org.velezreyes.quiz.question6;

public class Drink {
    private String name;
    private int price;
    private boolean isFizzy;

    public Drink(String name, int price, boolean isFizzy) {
        this.name = name;
        this.price = price;
        this.isFizzy = isFizzy;
    }

    public String getName() {
        return name;
    }

    public int getPrice() {
        return price;
    }

    public boolean isFizzy() {
        return isFizzy;
    }
}
