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
        required property photo -> str;
        required property birthday -> datetime;
        required property bio -> str;
        required property hash -> str;
        required property email -> str;
        required property username -> str;
    }

    abstract type Employer extending Person {
    }
}

module default {
    type Worker extending meta::Person {
        required property resume -> str;
        required property skills -> array<str>;
    }

    type Token extending meta::Created {
        required property value -> str;
        required link owner -> meta::Person;
    }
}
