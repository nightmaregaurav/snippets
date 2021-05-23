// package AdvJavaLab.RMIClient;

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;


public class Client {
    public static void main(String[] args) {
        try {
            RemoteAdder stub = (RemoteAdder)Naming.lookup("rmi://localhost:5000/adder");
            System.out.println(stub.add(1,2));
        } catch (RemoteException | MalformedURLException | NotBoundException e) {
            e.printStackTrace();
        }
    }
}
