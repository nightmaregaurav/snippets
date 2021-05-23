// package AdvJavaLab.RMIServer;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class Adder extends UnicastRemoteObject implements RemoteAdder{
    Adder() throws RemoteException{
        super(5000);
    }
    @Override
    public int add(int a, int b) {
        return a+b;
    }
}
