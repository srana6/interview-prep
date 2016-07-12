package general;

import java.util.*;


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



public class Apple {
	public static void main(String[] args) {
	    API api = new API();
	    api.addDepartment("Engineer");
	    api.addDepartment("SWTesting"); 
	    
	    
	    api.addManager("Manager1", 25, 120040, "Engineer");
	    api.addManager("Manager3", 27, 110000, "SWTesting");
	    
	    api.addEmployee("Employee1",29, 80672,  "Engineer" ,  "Manager1");
	    api.addEmployee("Employee6",25, 90234,  "SWTesting" , "Manager1");
	    api.addEmployee("Employee3",22, 60534,  "HWTesting" , "Manager3");
	    
	    
	    HashSet<Department> departments = api.getUniqueDepartmentsGivenManager("Manager1");
	    for (Department dept : departments){
	    	System.out.println(dept.name);
	    }
	    

	}

}
