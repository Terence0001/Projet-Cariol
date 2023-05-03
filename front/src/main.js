import { createApp } from 'vue'
import { createVuetify } from 'vuetify'
import App from './App.vue'

import 'vuetify/styles'
import './assets/main.css'

//VUETIFY COMPONENTS
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives
})
createApp(App).use(vuetify).mount('#app')
