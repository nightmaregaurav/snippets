/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

/**
 *
 * @author nightmare
 */
public class Adder extends UnicastRemoteObject implements AdderSkeleton {
    Adder() throws RemoteException{
        super();
    }
    
    @Override
    public int add(int a, int b) {
        // Actual operation
        return a+b;
    }
}
