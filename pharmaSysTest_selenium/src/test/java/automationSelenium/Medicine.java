package automationSelenium;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class Medicine {
    public static void main(String[] args) {
        WebDriverManager.edgedriver().setup();
        WebDriver driver = new EdgeDriver();

        driver.manage().window().maximize();
        driver.get("http://127.0.0.1:5500/frontend/login.html");
        WebElement usernameTextBox = driver.findElement(By.id("username"));
        usernameTextBox.sendKeys("admin");
        WebElement passwordTextBox = driver.findElement(By.id("password"));
        passwordTextBox.sendKeys("admin123");
        WebElement loginButton = driver.findElement(By.id("loginBtn"));
        loginButton.click();

        // Wait until dashboard loads
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        wait.until(ExpectedConditions.urlContains("dashboard"));

        // Open Medicine
        driver.get("http://127.0.0.1:5500/frontend/medicine.html");
        // Add Medicine
        WebElement editMedicine = driver.findElement(By.className("px-4"));
        editMedicine.click();
        WebElement addMedicine = driver.findElement(By.id("medName"));
        addMedicine.sendKeys("Medicine Name");

        // Edit Medicine
//        WebElement editButton = driver.findElement(By.className("btn-action"));
//        editButton.click();


    }
}
