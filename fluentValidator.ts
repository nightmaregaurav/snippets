class Validate {
  private value: any;
  private errors: string[];

  constructor(value: any) {
    this.value = value;
    this.errors = [];
  }

  public static from(value: any): Validate {
    return new Validate(value);
  }

  public isNullish(): Validate {
    if (this.value === null || this.value === undefined) {
      this.errors.push('Value must not be null or undefined.');
    }
    return this;
  }

  public isString(): Validate {
    if (typeof this.value !== 'string') {
      this.errors.push('Value must be a string.');
    }
    return this;
  }

  public isNumeric(): Validate {
    if (!/^-?\d*\.?\d+$/.test(this.value)) {
      this.errors.push('Value must be numeric.');
    }
    return this;
  }

  public isNumber(): Validate {
    if (typeof this.value !== 'number' || isNaN(this.value)) {
      this.errors.push('Value must be a valid number.');
    }
    return this;
  }

  public isObject(): Validate {
    if (typeof this.value !== 'object' || this.value === null || Array.isArray(this.value)) {
      this.errors.push('Value must be an object.');
    }
    return this;
  }

  public isArray(): Validate {
    if (!Array.isArray(this.value)) {
      this.errors.push('Value must be an array.');
    }
    return this;
  }

  public isLessThan(limit: number | string): Validate {
    if (typeof this.value !== 'number' && typeof this.value !== 'string') {
      throw new Error('isLessThan can only be applied to numbers and strings.');
    }
    if (this.value >= limit) {
      this.errors.push(`Value must be less than ${limit}.`);
    }
    return this;
  }

  public isMoreThan(limit: number | string): Validate {
    if (typeof this.value !== 'number' && typeof this.value !== 'string') {
      throw new Error('isMoreThan can only be applied to numbers and strings.');
    }
    if (this.value <= limit) {
      this.errors.push(`Value must be greater than ${limit}.`);
    }
    return this;
  }

  public equals(expectedValue: any): Validate {
    if (this.value !== expectedValue) {
      this.errors.push(`Value must be equal to ${expectedValue}.`);
    }
    return this;
  }

  public matchesRegex(regex: RegExp): Validate {
    if (!regex.test(this.value)) {
      this.errors.push('Value does not match the expected format.');
    }
    return this;
  }

  public contains(substring: string): Validate {
    if (typeof this.value !== 'string' || this.value.indexOf(substring) === -1) {
      this.errors.push(`Value must contain the substring '${substring}'.`);
    }
    return this;
  }

  public hasLength(length: number): Validate {
    if (typeof this.value !== 'string' && !Array.isArray(this.value)) {
      throw new Error('hasLength can only be applied to strings and arrays.');
    }
    if (this.value.length !== length) {
      this.errors.push(`Value must have a length of ${length}.`);
    }
    return this;
  }

  public evaluate(): { bool: boolean; errors: string[] } {
    return { bool: this.errors.length === 0, errors: this.errors };
  }
}
