class Ensure {
  private value: any;
  private errors: string[];

  constructor(value: any) {
    this.value = value;
    this.errors = [];
  }

  public static given(value: any): Validate {
    return new Validate(value);
  }

  public isNullish(): Validate {
    if (this.value !== null && this.value !== undefined) {
      this.errors.push('Value must be null or undefined.');
    }
    return this;
  }

  public isNotNullish(): Validate {
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

  public isNotString(): Validate {
    if (typeof this.value === 'string') {
      this.errors.push('Value must not be a string.');
    }
    return this;
  }

  public isNumeric(): Validate {
    if (!/^-?\d*\.?\d+$/.test(this.value)) {
      this.errors.push('Value must be numeric.');
    }
    return this;
  }

  public isNotNumeric(): Validate {
    if (/^-?\d*\.?\d+$/.test(this.value)) {
      this.errors.push('Value must not be numeric.');
    }
    return this;
  }

  public isNumber(): Validate {
    if (typeof this.value !== 'number' || isNaN(this.value)) {
      this.errors.push('Value must be a valid number.');
    }
    return this;
  }

  public isNotNumber(): Validate {
    if (typeof this.value === 'number' && !isNaN(this.value)) {
      this.errors.push('Value must not be a valid number.');
    }
    return this;
  }

  public isObject(): Validate {
    if (typeof this.value !== 'object' || this.value === null || Array.isArray(this.value)) {
      this.errors.push('Value must be an object.');
    }
    return this;
  }

  public isNotObject(): Validate {
    if (typeof this.value === 'object' && this.value !== null && !Array.isArray(this.value)) {
      this.errors.push('Value must not be an object.');
    }
    return this;
  }

  public isArray(): Validate {
    if (!Array.isArray(this.value)) {
      this.errors.push('Value must be an array.');
    }
    return this;
  }

  public isNotArray(): Validate {
    if (Array.isArray(this.value)) {
      this.errors.push('Value must not be an array.');
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

  public isNotLessThan(limit: number | string): Validate {
    if (typeof this.value !== 'number' && typeof this.value !== 'string') {
      throw new Error('isNotLessThan can only be applied to numbers and strings.');
    }
    if (this.value < limit) {
      this.errors.push(`Value must not be less than ${limit}.`);
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

  public isNotMoreThan(limit: number | string): Validate {
    if (typeof this.value !== 'number' && typeof this.value !== 'string') {
      throw new Error('isNotMoreThan can only be applied to numbers and strings.');
    }
    if (this.value > limit) {
      this.errors.push(`Value must not be greater than ${limit}.`);
    }
    return this;
  }

  public startsWith(substring: string): Validate {
    if (typeof this.value !== 'string' && !Array.isArray(this.value)) {
      throw new Error('startsWith can only be applied to strings and arrays.');
    }
    if (!this.value.startsWith(substring)) {
      this.errors.push(`Value must start with the substring '${substring}'.`);
    }
    return this;
  }

  public doesNotStartWith(substring: string): Validate {
    if (typeof this.value === 'string' && !Array.isArray(this.value)) {
      if (this.value.startsWith(substring)) {
        this.errors.push(`Value must not start with the substring '${substring}'.`);
      }
    } else {
      throw new Error('doesNotStartWith can only be applied to strings and arrays.');
    }
    return this;
  }

  public endsWith(substring: string): Validate {
    if (typeof this.value !== 'string' && !Array.isArray(this.value)) {
      throw new Error('endsWith can only be applied to strings and arrays.');
    }
    if (!this.value.endsWith(substring)) {
      this.errors.push(`Value must end with the substring '${substring}'.`);
    }
    return this;
  }

  public doesNotEndWith(substring: string): Validate {
    if (typeof this.value === 'string' && !Array.isArray(this.value)) {
      if (this.value.endsWith(substring)) {
        this.errors.push(`Value must not end with the substring '${substring}'.`);
      }
    } else {
      throw new Error('doesNotEndWith can only be applied to strings and arrays.');
    }
    return this;
  }

  public equals(expectedValue: any): Validate {
    if (this.value !== expectedValue) {
      this.errors.push(`Value must be equal to ${expectedValue}.`);
    }
    return this;
  }

  public isNotEqual(expectedValue: any): Validate {
    if (this.value === expectedValue) {
      this.errors.push(`Value must not be equal to ${expectedValue}.`);
    }
    return this;
  }

  public matchesRegex(regex: RegExp): Validate {
    if (!regex.test(this.value)) {
      this.errors.push('Value does not match the expected format.');
    }
    return this;
  }

  public doesNotMatchRegex(regex: RegExp): Validate {
    if (regex.test(this.value)) {
      this.errors.push('Value must not match the expected format.');
    }
    return this;
  }

  public contains(substring: string): Validate {
    if (typeof this.value !== 'string' || this.value.indexOf(substring) === -1) {
      this.errors.push(`Value must contain the substring '${substring}'.`);
    }
    return this;
  }

  public doesNotContain(substring: string): Validate {
    if (typeof this.value === 'string' && this.value.indexOf(substring) !== -1) {
      this.errors.push(`Value must not contain the substring '${substring}'.`);
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

  public doesNotHaveLength(length: number): Validate {
    if (typeof this.value === 'string' || Array.isArray(this.value)) {
      if (this.value.length === length) {
        this.errors.push(`Value must not have a length of ${length}.`);
      }
    } else {
      throw new Error('doesNotHaveLength can only be applied to strings and arrays.');
    }
    return this;
  }

  public evaluate(): { isValid: boolean; errors: string[] } {
    return { isValid: this.errors.length === 0, errors: this.errors };
  }
}
