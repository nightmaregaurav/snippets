/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.ResultSet;
import java.sql.Statement;
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
            
            Statement statement = connection.createStatement();
            
            System.out.println("Create Table");
            sql = "CREATE TABLE IF NOT EXISTS crud(id int PRIMARY KEY AUTO_INCREMENT, `key` VARCHAR(40), `value` VARCHAR(50))";
            statement.execute(sql);
            
            System.out.println("Insert");
            sql = "INSERT INTO crud(`key`, `value`) VALUES ('one', '1'), ('two', '2')";
            statement.executeUpdate(sql);
            
            sql = "SELECT * FROM crud";
            ResultSet resultset = statement.executeQuery(sql);
            
            while (resultset.next()) {
                System.out.println(resultset.getString("key") + ": " + resultset.getString("value"));
            }
            
            System.out.println("Update");
            sql = "UPDATE crud set `key`='ONE' WHERE id=1";
            statement.executeUpdate(sql);
            
            sql = "SELECT * FROM crud";
            resultset = statement.executeQuery(sql);
            
            while (resultset.next()) {
                System.out.println(resultset.getString("key") + ": " + resultset.getString("value"));
            }

            System.out.println("Delete");
            sql = "DELETE FROM crud WHERE id=2";
            statement.executeUpdate(sql);

            sql = "SELECT * FROM crud";
            resultset = statement.executeQuery(sql);
            
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
