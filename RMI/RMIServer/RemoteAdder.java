// package AdvJavaLab.RMIServer;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface RemoteAdder extends Remote {
    int add(int a, int b) throws RemoteException;
}
