package test01;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.edge.EdgeDriver;
import org.testng.annotations.Test;

public class TaxtTest {
    protected WebDriver driver;

    @Test
    void setup(){
        WebDriverManager.edgedriver().setup();
        driver = new EdgeDriver();
        driver.manage().window().maximize();
        driver.get("https://www.taxadvisor.lk/calculator/cal-2025");

        WebElement amount = driver.findElement(By.name("amountA"));
        amount.sendKeys("450000");

        WebElement submitbtn = driver.findElement(By.id("submit"));
        submitbtn.click();
    }
}
