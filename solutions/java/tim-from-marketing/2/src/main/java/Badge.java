class Badge {
    public String print(Integer id, String name, String department) {
        if (id == null) {
            if (department == null) {
                return name + " - OWNER";
        } else {
            return name + " - " + department.toUpperCase();
        }
        }
        if (department == null) {
            return "[" + id + "]" + " - " + name + " - OWNER";
        }
        return "[" + id + "]" + " - " + name + " - " + department.toUpperCase();
    }
}
