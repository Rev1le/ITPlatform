module meta {
    abstract type Created {
        required property created_at -> datetime {
          readonly := true;
          default := datetime_current();
        }
    }

    abstract type Person extending Created {
        required property name -> str {
            constraint max_len_value(1024);
        }

        required property birthday -> datetime;
        required property hash -> str;
        required property email -> str {
            constraint exclusive;
        }
        property bio -> str;
        property photo -> str;
        multi link tokens := .<owner[is default::Token]
    }

    abstract type Task extending Created {
    }
}

module default {
    type Worker extending meta::Person {
        property resume -> str;
        property skills -> array<str>;
    }

    type Token extending meta::Created {
        required property value -> str;
        required link owner -> meta::Person;
    }

    type Employer extending meta::Person {
        link recruiter := .<employer[is Recruiter];
    }

    type Vacancy extending meta::Created {
        required property name -> str;
        required property about -> str;
        required property skills -> array<str>;
        required property company -> str;
        property salary -> float32;
    }

    type Recruiter extending meta::Created {
        required link employer -> Employer;
        multi link vacancies -> Vacancy;
    }

    type TaskQuestion extending meta::Task {
        required property question -> str;
        required property answers -> array<str>;
        required property right_answer -> str;
    }

    type TaskCodeTest extending meta::Created {
        required property input -> str;
        required property output -> str;
    }

    type TaskCode extending meta::Task {
        required property question -> str;
        multi link tests -> TaskCodeTest;
    }

    type TaskBlock extending meta::Task {
        required property name -> str;
        required property difficulty -> int;
    }
}
