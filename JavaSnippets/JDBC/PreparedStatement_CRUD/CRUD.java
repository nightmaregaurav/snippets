/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
public class CRUD {
    public static void main(String[] args) {
        try {
            String url = "jdbc:mysql://localhost:3306/";
            String db = "test";
            String driver = "com.mysql.cj.jdbc.Driver";
            String username = "pma";
            String password = "pma";
            String sql = "";
            
            System.out.println("Connection");
            Class.forName(driver);
            
            Connection connection = DriverManager.getConnection(url+db, username, password);
            
            System.out.println("Create Table");
            sql = "CREATE TABLE IF NOT EXISTS crud(id int PRIMARY KEY AUTO_INCREMENT, `key` VARCHAR(40), `value` VARCHAR(50))";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.execute();
            
            System.out.println("Insert");
            sql = "INSERT INTO crud(`key`, `value`) VALUES (?, ?), (?, ?)";
            preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setString(1, "one");
            preparedStatement.setString(2, "1");
            preparedStatement.setString(3, "two");
            preparedStatement.setString(4, "2");
            preparedStatement.executeUpdate();
            
            sql = "SELECT * FROM crud";
            preparedStatement = connection.prepareStatement(sql);
            ResultSet resultset = preparedStatement.executeQuery();
            
            while (resultset.next()) {
                System.out.println(resultset.getString("key") + ": " + resultset.getString("value"));
            }
            
            System.out.println("Update");
            sql = "UPDATE crud set `key`=? WHERE id=?";
            preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setString(1, "ONE");
            preparedStatement.setInt(2, 1);
            preparedStatement.executeUpdate();
            
            sql = "SELECT * FROM crud";
            preparedStatement = connection.prepareStatement(sql);
            resultset = preparedStatement.executeQuery();
            
            while (resultset.next()) {
                System.out.println(resultset.getString("key") + ": " + resultset.getString("value"));
            }

            System.out.println("Delete");
            sql = "DELETE FROM crud WHERE id=?";
            preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setInt(1, 2);
            preparedStatement.executeUpdate();

            sql = "SELECT * FROM crud";
            preparedStatement = connection.prepareStatement(sql);
            resultset = preparedStatement.executeQuery();
            
            while (resultset.next()) {
                System.out.println(resultset.getString("key") + ": " + resultset.getString("value"));
            }
            
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(CRUD.class.getName()).log(Level.SEVERE, null, ex);
        } catch (SQLException ex) {
            Logger.getLogger(CRUD.class.getName()).log(Level.SEVERE, null, ex);
        }

    }
}
