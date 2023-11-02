package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

public class VendingMachineImpl implements VendingMachine {

    private static VendingMachine instance = new VendingMachineImpl();
    private int quarterCount = 0;
    private Map<String, Drink> drinkSelection;

    private VendingMachineImpl() {
        drinkSelection = new HashMap<>();
        drinkSelection.put("ScottCola", new Drink("ScottCola", 3, true));
        drinkSelection.put("KarenTea", new Drink("KarenTea", 4, false));
    }

    public static VendingMachine getInstance() {
        return instance;
    }

    @Override
    public void insertQuarter() {
        quarterCount++;
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        if (!drinkSelection.containsKey(name)) {
            throw new UnknownDrinkException();
        }
        Drink selectedDrink = drinkSelection.get(name);
        if (quarterCount < selectedDrink.getPrice()) {
            throw new NotEnoughMoneyException();
        }
        quarterCount -= selectedDrink.getPrice();
        quarterCount = 0;
        return selectedDrink;
    }
}
