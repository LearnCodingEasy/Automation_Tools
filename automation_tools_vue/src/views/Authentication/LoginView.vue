
<template>
  <div class="wrapper_page_login">
    <div class="inner_page_login">
      <div class="container mx-auto">
        <div class="wrapper_content_page_login">
          <div
            class="inner_content_page_login w-full mobile_grid_12 tablet_grid_12 laptop_grid_12 laptop_lg_grid_12 desktop_grid_12 desktop_lg_grid_12"
          >
            <!-- Signup -->
            <div
              class="box_content_page_login mobile_item_12 tablet_item_12 laptop_item_6 laptop_lg_item_6 desktop_item_6 desktop_lg_item_6"
            >
              <div class="mobile_body_dark">
                <span class="voice_up"> </span>
                <span class="voice_down"> </span>
                <span class="power"> </span>
                <span class="sonser"> </span>
                <span class="voice"> </span>
                <span class="carme"> </span>
                <div class="mobile_content">
                  <form class="">
                    <prime_card class="prime_card_form_signup">
                      <template #header>
                        <div class="flex justify-between items-center w-full">
                          <div class="text font-bold text-5xl">Signup</div>
                          <div class="image_logo">
                            <img src="../../assets/Images/Messenger_80x80.png" class="" alt="" />
                          </div>
                        </div>
                      </template>
                      <template #content>
                        <prime_fluid class="prime_card_form_signup_content">
                          <div class="">
                            <div class="flex">
                              <!-- First name -->
                              <div class="mr-1">
                                <prime_input_text
                                  type="text"
                                  placeholder="First name"
                                  v-model="formSignup.name"
                                />
                              </div>
                              <!-- Surname -->
                              <div class="ml-1">
                                <prime_input_text
                                  placeholder="Surname"
                                  v-model="formSignup.surname"
                                />
                              </div>
                            </div>
                            <!-- Mobile number or email address -->
                            <div class="col-span-full">
                              <prime_input_text
                                placeholder="Mobile number or email address"
                                v-model="formSignup.email"
                              />
                            </div>
                            <!-- password1 -->
                            <div class="col-span-full">
                              <prime_input_password
                                placeholder="New Password"
                                v-model="formSignup.password1"
                                autocomplete="off"
                              />
                            </div>
                            <!-- password2 -->
                            <div class="col-span-full">
                              <prime_input_password
                                placeholder="Repeat password"
                                v-model="formSignup.password2"
                                autocomplete="off"
                              />
                            </div>
                            <!-- Date of birth -->
                            <div class="col-span-full">Date of birth</div>
                            <div class="col-span-full">
                              <div class="flex flex-col md:flex-row gap-2">
                                <!-- Day -->
                                <prime_input_group>
                                  <prime_date_picker v-model="day" view="day" dateFormat="dd" />
                                </prime_input_group>
                                <!-- Month -->
                                <prime_input_group>
                                  <prime_date_picker v-model="month" view="month" dateFormat="mm" />
                                </prime_input_group>
                                <!-- Year -->
                                <prime_input_group>
                                  <prime_date_picker v-model="year" view="year" dateFormat="yy" />
                                </prime_input_group>
                              </div>
                            </div>
                            <!-- Gender -->
                            <div class="col-span-full">Gender</div>
                            <div class="flex flex-col md:flex-row gap-2">
                              <prime_input_group>
                                <prime_radio_button
                                  v-model="formSignup.gender"
                                  inputId="ingredient1"
                                  name="gender"
                                  value="Female"
                                />
                                <label for="ingredient1" class="ml-2"> Female </label>
                              </prime_input_group>
                              <prime_input_group>
                                <prime_radio_button
                                  v-model="formSignup.gender"
                                  inputId="ingredient2"
                                  name="gender"
                                  value="Male"
                                />
                                <label for="ingredient2" class="ml-2"> Male </label>
                              </prime_input_group>

                              <prime_input_group>
                                <prime_radio_button
                                  v-model="formSignup.gender"
                                  inputId="ingredient3"
                                  name="gender"
                                  value="Custom"
                                />
                                <label for="ingredient3" class="ml-2"> Custom </label>
                              </prime_input_group>
                            </div>
                          </div>
                        </prime_fluid>
                      </template>
                      <template #footer>
                        <div class="flex justify-center gap-2">
                          <button
                            type="submit"
                            class="d_block_important mt-1 mx-auto w_50 btn_signup py-3 px-5 rounded"
                            @click.prevent="submitFormSignup"
                          >
                            Signup
                          </button>
                        </div>
                      </template>
                      <!-- Errors -->
                      <template v-if="errorsSignup.length > 0">
                        <prime_toast />
                      </template>
                    </prime_card>
                  </form>
                </div>
              </div>
            </div>
            <!-- Log in -->
            <div
              class="box_content_page_login mobile_item_12 tablet_item_12 laptop_item_6 laptop_lg_item_6 desktop_item_6 desktop_lg_item_6"
            >
              <div class="mobile_body_white">
                <span class="voice_up"> </span>
                <span class="voice_down"> </span>
                <span class="power"> </span>
                <span class="sonser"> </span>
                <span class="voice"> </span>
                <span class="carme"> </span>
                <div class="mobile_content">
                  <form class="">
                    <prime_card class="prime_card_form_login">
                      <template #header>
                        <div class="flex justify-between items-center w-full">
                          <div class="text font-bold text-5xl">Log in</div>
                          <div class="image_logo">
                            <img src="../../assets/Images/Messenger_80x80.png" class="" alt="" />
                          </div>
                        </div>
                      </template>
                      <template #content>
                        <prime_fluid class="prime_card_form_login_content">
                          <div class="input_email">
                            <!-- Mobile number or email address -->
                            <div class="col-span-full">
                              <prime_input_text
                                placeholder="Mobile number or email address"
                                v-model="formLogin.email"
                              />
                            </div>
                          </div>
                          <!-- password -->
                          <div class="col-span-full">
                            <prime_input_password
                              placeholder="Your Password"
                              v-model="formLogin.password"
                              autocomplete="off"
                            />
                          </div>
                        </prime_fluid>
                        <div class="Forgotten_password mt-4">
                          <a href="#" class="text-blue-600 mx-auto my-2 block text-center"
                            >Forgotten password?</a
                          >
                          <hr />
                          <div class="block w-full my-4">
                            <div class="social-login flex justify-between items-center">
                              <!-- @click="visible = true" -->
                              <prime_button
                                icon="pi pi-google"
                                label="تسجيل "
                                severity="success"
                                class="class_name"
                                @click="loginWithGoogle"
                              />
                              <!-- @click="visible = true" -->
                              <prime_button
                                icon="pi pi-facebook"
                                label="تسجيل "
                                severity="info"
                                class="class_name"
                                @click="loginWithFacebook"
                              />
                            </div>
                          </div>
                        </div>
                      </template>
                      <template #footer>
                        <div class="row">
                          <!-- Errors -->
                          <template v-if="errorsLogin.length > 0">
                            <prime_toast></prime_toast>
                          </template>
                          <!-- Login -->
                          <div class="mt-2">
                            <button
                              type="submit"
                              class="d_block_important mt-1 mb-2 mx-auto py-3 px-5 rounded btn_login"
                              @click.prevent="submitFormLogin"
                            >
                              Log In
                            </button>

                            <!-- Button Signup -->
                          </div>
                        </div>
                      </template>
                    </prime_card>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <prime_toast />
  </div>
</template>

<script>
import axios from 'axios'
// eslint-disable-next-line no-unused-vars
import { RouterLink } from 'vue-router'
import { useUserStore } from '@/stores/user'

export default {
  name: 'LoginView',
  components: {},

  setup() {
    const userStore = useUserStore()
    return {
      userStore,
    }
  },
  data() {
    return {
      formLogin: {
        email: '',
        password: '',
      },
      errorsLogin: [],

      // Signup
      formSignup: {
        name: '',
        surname: '',
        email: '',
        date_of_birth: null,
        gender: '',
        password1: '',
        password2: '',
      },
      day: '',
      month: '',
      year: '',
      errorsSignup: [],
    }
  },
  methods: {
    async submitFormLogin() {
      this.errorsLogin = []
      if (this.formLogin.email === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User Name missing',
          detail: 'Your name is missing',
          life: 3000,
        })
        this.errorsLogin.push('Your e-mail is missing')
      }
      if (this.formLogin.password === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User password is missing',
          detail: 'Your password is missing',
          life: 3000,
        })
        this.errorsLogin.push('Your password is missing')
      }
      // Login
      if (this.errorsLogin.length === 0) {
        await axios
          .post('/api/login/', this.formLogin)
          .then((response) => {
            this.userStore.setToken(response.data)
            console.log('response.data: ', response.data)
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access
          })
          .catch((error) => {
            console.error('Error ', error)
            console.error('Error Message', error.message)
            this.$toast.add({
              severity: 'error',
              summary: 'Error From Login',
              detail: `${error.message}`,
              life: 6000,
            })
            /*
              if (error.response.data.detail) {
                            // Code If True
                            this.$toast.add({
                              severity: 'error',
                              summary: 'Error Message',
                              detail: `${error.response.data.detail}`,
                              life: 6000,
                            })
                          }
              */
            this.errorsLogin.push(
              'The email or password is incorrect! Or the user is not activated!',
            )
          })
      }
      // Me
      if (this.errorsLogin.length === 0) {
        await axios
          .get('/api/me/')
          .then((response) => {
            this.userStore.setUserInfo(response.data)
            this.$router.push('/')
          })
          .catch((error) => {
            console.log('error', error)
            this.$toast.add({
              severity: 'error',
              summary: 'Error From Login Me',
              detail: `${error.message}`,
              life: 6000,
            })
          })
      }
    },
    submitFormSignup() {
      this.errorsSignup = []

      if (this.formSignup.name === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User Name missing',
          detail: 'Your name is missing',
          life: 3000,
        })
        this.errorsSignup.push('Your name is missing')
      }
      if (this.formSignup.surname === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User Surname missing',
          detail: 'Your Surname is missing',
          life: 3000,
        })
        this.errorsSignup.push('Your surname is missing')
      }
      if (this.formSignup.email === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User Is missing',
          detail: 'Your e-mail is missing',
          life: 3000,
        })
        this.errorsSignup.push('Your e-mail is missing')
      }
      if (this.formSignup.password1 === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User passwordIs missing',
          detail: 'Your password is missing',
          life: 3000,
        })
        this.errorsSignup.push('Your password is missing')
      }
      if (this.formSignup.password1 !== this.formSignup.password2) {
        this.$toast.add({
          severity: 'error',
          summary: 'User  password does not match',
          detail: 'Your password  does not match',
          life: 3000,
        })
        this.errorsSignup.push('The password does not match')
      }

      // 🗓️ استخراج اليوم، الشهر، والسنة من كائنات Date وتنسيقها
      if (this.day === '') {
        this.$toast.add({
          severity: 'warn', // ⚠️
          summary: 'Day Missing 🗓️',
          detail: '⚠️ User Date Of Birth missing [Day]',
          life: 3000,
        })
        this.errorsSignup.push('❌ User Date Of Birth missing [Day]')
      } else if (this.month === '') {
        this.$toast.add({
          severity: 'warn', // ⚠️
          summary: 'Month Missing 📅',
          detail: '⚠️ User Date Of Birth missing [Month]',
          life: 3000,
        })
        this.errorsSignup.push('❌ User Date Of Birth missing [Month]')
      } else if (this.year === '') {
        this.$toast.add({
          severity: 'warn', // ⚠️
          summary: 'Year Missing 📆',
          detail: '⚠️ User Date Of Birth missing [Year]',
          life: 3000,
        })
        this.errorsSignup.push('❌ User Date Of Birth missing [Year]')
      } else {
        const day = this.day.getDate().toString().padStart(2, '0') // 🗓️
        const month = (this.month.getMonth() + 1).toString().padStart(2, '0') // 📅
        const year = this.year.getFullYear() // 📆

        const formattedDate = `${year}-${month}-${day}` // 📝
        this.formSignup.date_of_birth = formattedDate // ✅ تم تسجيل التاريخ بنجاح
      }
      if (this.errorsSignup.length === 0) {
        axios
          .post('/api/signup/', this.formSignup)
          .then((response) => {
            if (response.data.message === 'success') {
              if (response.data.email_sent) {
                this.$toast.add({
                  severity: 'success',
                  summary: 'User Registered',
                  detail: 'Please activate your account by clicking the link sent to your email.',
                  life: 3000,
                })
              }
              this.$toast.add({
                severity: 'success',
                summary: 'User Is Registered',
                detail: 'Please activate your account by clicking your email link',
                life: 3000,
              })
              this.formSignup.name = ''
              this.formSignup.surname = ''
              this.formSignup.email = ''
              this.formSignup.date_of_birth = ''
              this.formSignup.gender = ''
              this.formSignup.password1 = ''
              this.formSignup.password2 = ''
              // this.$router.push('/loginView')
              window.location.reload()
            } else {
              // 🔄 تحليل البيانات المستلمة من الاستجابة
              const data = JSON.parse(response.data.message)
              for (const key in data) {
                // 🚨 إضافة رسالة الخطأ إلى قائمة الأخطاء
                this.errorsSignup.push(data[key][0].message)
                // 📧 التحقق إذا كان البريد الإلكتروني موجود مسبقًا
                if (data[key][0].message == 'User with this Email already exists.') {
                  this.$toast.add({
                    severity: 'warn', // ⚠️
                    summary: 'Warning 📧',
                    detail: ' Please Login Now',
                    life: 6000,
                  })
                }
                // 📅 التحقق من صحة تاريخ الميلاد
                if (data[key][0].date_of_birth == 'Enter a valid date.') {
                  this.$toast.add({
                    severity: 'warn', // ⚠️
                    summary: 'Invalid Date 📅',
                    detail: '⚠️ Please Enter a valid date. 📆',
                    life: 6000,
                  })
                }
              }
            }
          })
          .catch((error) => {
            console.log('error', error)
            console.log('error', error.message)
            // if (error.message == 'User with this Email already exists.') {
            //   this.$toast.add({
            //     severity: 'error',
            //     summary: 'Error Message',
            //     detail: ' Please Login Now',
            //     life: 6000,
            //   })
            // }
          })
      }
    },
    loginWithGoogle() {
      // window.location.href = 'Google: http://127.0.0.1:8000/social/login/google-oauth2/'
      window.location.href = "http://127.0.0.1:8000/accounts/google/login/";

    },
    loginWithFacebook() {
      window.location.href = 'http://127.0.0.1:8000/accounts/facebook/login/'
    },
  },
  mounted() {
    // 📝 عنوان الصفحة
    document.title = 'Account | Authentication'
  },
}
</script>

<style lang="scss"></style>

        