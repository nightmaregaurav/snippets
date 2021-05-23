// package AdvJavaLab.RMIServer;

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;

public class Server {
    public static void main(String[] args) {
        try {
            LocateRegistry.createRegistry(5000);
            RemoteAdder stub = new Adder();
            Naming.rebind("rmi://localhost:5000/adder",stub);
        } catch (RemoteException | MalformedURLException e) {
            e.printStackTrace();
        }
    }
}
