import java.io.*;
import java.util.*;

 /*
 * To execute Java, please define "static void main" on a class
 * named Solution.
 *
 * If you need more classes, simply define them inline.
 
 Question
  1. In a organisation, establish a employee, Manager and Department relationship.
  2. A Manager can have employees from multiple Departments
  3. Similarly department can have employees who report diffrent managers
  4. Provide API/Methods to add a new employee/Manager/Department and store it in-memory. for ex: addDepartment, addEmployee, addManager
  5. For every employee maintain their name, age and Salary
         
         
   Employee
   
   Manager   ->  Employees  
   
   Department   - > Employees
         
         
         
 */

/* Sample data to load 

  Department
    Engineer - Engineering Stream  
    HWTesting -  Hardware Testing
    SWTesting - Software Testing
    
  Employee
    Employee1  Engineer   Manager1  29 80672
    Employee2  Engineer   Manager2  23 70224
    Employee3  HWTesting  Manager3  22 60534
    Employee4  HWTesting  Manager3  22 40234
    Employee5  Engineer   Manager2  24 60234
    Employee6  SWTesting  Manager1  25 90234
    Employee7  HWTesting  Manager3  28 70234
    
  Manager
    Manager1 Engineer 25 120040
    Manager2 SWTesting 29 120500
    Manager3 SWTesting 27 110000
    
  ----------------------------------  
  
  Person -> name, age, salary, department
  Employee, Manager   ->  Person
    
  Manager -> list  employees  (managed)

*/


class Department {
    ArrayList<Person> list_person;
    String name;
  
    public Department(String name){
       this.name = name;
       this.list_person = new ArrayList<Person>();
    }
  
    public void addPerson(Person person){
       list_person.add(person);
    }
  
}

abstract class Person {
    String name;
    int age;
    double salary;
    Department department;
  
   public Person(String name, int age, double salary, Department department){
       this.name = name;
       this.age = age;
       this.salary = salary;
       this.department = department;
   }
}

class Employee extends Person {
  
   Manager manager;
  
   public Employee(String name, int age, double salary, Department department, Manager manager){
      super(name, age, salary, department);
      this.manager = manager;
   }
}

class Manager extends Person {
  
    ArrayList<Employee> employess;
  
  
    public Manager(String name, int age, double salary, Department department){
      super(name, age, salary, department);
      this.employess = new ArrayList<Employee>();
   }
  
   public void addEmployee(Employee employee){
      this.employess.add(employee);
   }
}






class API {
  
    HashMap<String, Department> departments;
    HashMap<String, Employee> employees;
    HashMap<String, Manager> managers;
  
    public API() {
         departments = new HashMap<String, Department>();
         employees = new HashMap<String, Employee>();
         managers = new HashMap<String, Manager>();
    }

	//Given a manager name, list unique departments that his employees belong to.    
    public HashSet<Department> getUniqueDepartmentsGivenManager(String manager_name){
         Manager manager = managers.get(manager_name);
         if (manager == null) 
           return null;
      
         HashSet<Department> unique_dep =  new HashSet<Department>();
         
         ArrayList<Employee> employees = manager.employess;
         for (int i = 0; i < employees.size() ; i++){
             Department department = employees.get(i).department;
             unique_dep.add(department);         
         }              
            
         return unique_dep;         
    }
  
  
    public void addDepartment(String name){
       Department department = new Department(name);
       departments.put(name, department);
    }
  
    public boolean addEmployee(String name, int age, double salary, String department_name, String manager_name){
       Department department = departments.get(department_name);
       if (department == null) 
           return false;
      
       Manager manager = managers.get(manager_name);
       if (manager == null) 
           return false;
      
      
       Employee employee = new Employee(name, age, salary, department, manager);
       employees.put(name, employee);
       department.addPerson(employee);
       manager.addEmployee(employee);
       return true;
    }
  
    public boolean addManager(String name, int age, double salary, String department_name){
       Department department = departments.get(department_name);
       if (department == null) return false;
      
       Manager manager = new Manager(name, age, salary, department);
       department.addPerson(manager);
       managers.put(name, manager);
       return true;
    }

  
}



class Solution {  
  
  public static void main(String[] args) {
    ArrayList<String> strings = new ArrayList<String>();
    strings.add("Hello, World!");
    strings.add("Welcome to CoderPad.");
    strings.add("This pad is running Java 8.");

    for (String string : strings) {
      System.out.println(string);
    }
    
    
    
    
    API api = new API();
    api.addDepartment("Engineer");
    api.addDepartment("SWTesting"); 
    
    
    api.addManager("Manager1", 25, 120040, "Engineer");
    boolean t1 = api.addEmployee("Employee1",29, 80672,  "Engineer" , "Manager1");
    boolean t2 = api.addEmployee("Employee6",25, 90234,  "SWTesting" , "Manager1");
    
    
    System.out.println(t1 + "   " + t2);
    HashSet<Department> departments = api.getUniqueDepartmentsGivenManager("Manager1");
    
    
    
    
    
    //Employee test = new Employee("Employee1", 29, 80672, dep_test);
    //System.out.println(test.name);
    
  }
}



/* Sample data to load 

  Department
    Engineer - Engineering Stream  
    HWTesting -  Hardware Testing
    SWTesting - Software Testing
    
  Employee
    Employee1  Engineer   Manager1  29 80672
    Employee2  Engineer   Manager2  23 70224
    Employee3  HWTesting  Manager3  22 60534
    Employee4  HWTesting  Manager3 22 40234
    Employee5  Engineer   Manager2  24 60234
    Employee6  SWTesting  Manager1  25 90234
    Employee7  HWTesting  Manager3  28 70234
    
  Manager
    Manager1 Engineer 25 120040
    Manager2 SWTesting 29 120500
    Manager3 SWTesting 27 110000
    
  ----------------------------------  
  
  Person -> name, age, salary, department
  Employee, Manager   ->  Person
    
  Manager -> list  employees  (managed)

*/